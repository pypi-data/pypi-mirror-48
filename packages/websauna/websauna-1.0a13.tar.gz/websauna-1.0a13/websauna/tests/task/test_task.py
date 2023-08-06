"""Celery async task tests."""
# Standard Library
import os
import time

# Pyramid
import transaction

import pytest
from flaky import flaky

# Websauna
from websauna.system.devop.cmdline import init_websauna
from websauna.system.task.celery import get_celery
from websauna.system.user.models import User
from websauna.tests.task import demotasks


@pytest.fixture(scope='module')
def task_app_request(task_ini_file, ini_settings):
    return init_websauna(task_ini_file)


@pytest.fixture()
def demo_user(request, dbsession):
    """Create a database object asyncronously manipulated."""

    with transaction.manager:
        # Do a dummy database write
        u = User(username="test", email="test@example.com")
        dbsession.add(u)


@pytest.fixture(scope='module')
def celery_worker(request, task_ini_file, watcher_getter):
    """py.test fixture to shoot up Celery worker process to process our test tasks when scheduled."""
    # Uncomment this and run ws-celery from command line for debug
    # ws-celery ws://websauna/tests/task/task-test.ini -- worker --loglevel=debug
    # return
    ini_file = "ws://{}".format(task_ini_file)
    pid_file = "/tmp/celery.pid"
    # logger.info("Running celery worker: %s", cmdline)

    return watcher_getter(
        name='ws-celery',
        arguments=[ini_file, '--', 'worker', '--pidfile={}'.format(pid_file)],
        checker=lambda: os.path.exists(pid_file),
        request=request,
    )


@flaky
def test_transaction_aware_task_success(celery_worker, task_app_request, dbsession, demo_user):
    """Transaction aware tasks works in eager mode.."""
    with transaction.manager:
        # Do a dummy database write
        u = dbsession.query(User).first()

        demotasks.modify_username.apply_async([u.id], tm=transaction.manager)
        # Let the task travel in Celery queue
        time.sleep(2.0)

        # Task should not fire unless we exit the transaction
        assert u.username != "set by celery"

    # Let the transaction commit
    time.sleep(0.5)

    # Task has now fired after transaction was committed
    with transaction.manager:
        u = dbsession.query(User).get(1)
        assert u.username == "set by celery"


@flaky
def test_transaction_manager_abort(celery_worker, task_app_request, dbsession, demo_user):
    """Test that transaction are not executed to schedule if transaction manager aborts."""

    try:
        # Tasks do not execute if transaction is never commit because of exception
        with transaction.manager:
            assert dbsession.query(User).count() == 1
            assert dbsession.query(User).get(1).username == "test"
            demotasks.modify_username.apply_async(args=[1], tm=transaction.manager)
            raise RuntimeError("aargh")
    except RuntimeError:
        pass

    # Let the transaction commit (which should not happen)
    time.sleep(0.5)

    # Because of exception, Celery never fires
    with transaction.manager:
        u = dbsession.query(User).get(1)
        assert u.username == "test"


@flaky
def test_task_throws_exception(celery_worker, task_app_request, dbsession, demo_user):
    """Test that transaction aware task does not commit if exception is thrown.."""

    with transaction.manager:
        u = dbsession.query(User).first()
        demotasks.modify_username_abort_by_exception.apply_async(args=[u.id], tm=transaction.manager)

    # Let the Celery task execute
    time.sleep(0.5)

    with transaction.manager:
        # Value should not have changed
        u = dbsession.query(User).first()
        assert u.username == "test"


@flaky
def test_manual_transaction(celery_worker, task_app_request, dbsession, demo_user):
    """Manual transaction lifecycles within task work."""

    with transaction.manager:
        # Do a dummy database write
        u = dbsession.query(User).first()

        demotasks.modify_username_manual_transaction.apply_async(kwargs={"user_id": u.id}, tm=transaction.manager)
        # Let the task travel in Celery queue
        time.sleep(1.0)

        # Task should not fire unless we exit the transaction
        assert u.username != "set by celery"

    # Let the transaction commit
    time.sleep(0.5)

    # Task has now fired after transaction was committed
    with transaction.manager:
        u = dbsession.query(User).first()
        assert u.username == "set by celery"


@flaky
def test_eager(celery_worker, task_app_request, dbsession, demo_user):
    """When in eager mode, transactions are executed properly.."""

    celery = get_celery(task_app_request.registry)
    celery._conf["task_always_eager"] = True

    try:

        # Try RetryableTransactionTask in eager mode
        with transaction.manager:
            # Do a dummy database write
            u = dbsession.query(User).first()

            demotasks.modify_username.apply_async(args=[u.id], tm=transaction.manager)
            # Task should not execute until TM commits
            assert u.username != "set by celery"

        # TM commits the new result should be instantly available

        # Task has now fired after transaction was committed
        with transaction.manager:
            u = dbsession.query(User).first()
            assert u.username == "set by celery"

        # Let's test ScheduleOnCommitTask with manually managed transaction
        with transaction.manager:
            u = dbsession.query(User).first()
            u.username = "foobar"
            demotasks.modify_username_manual_transaction.apply_async(args=[u.id], tm=transaction.manager)

        # ScheduledOnCommitTask should have finished now
        with transaction.manager:
            u = dbsession.query(User).first()
            assert u.username == "set by celery"

    finally:
        celery._conf["task_always_eager"] = False
