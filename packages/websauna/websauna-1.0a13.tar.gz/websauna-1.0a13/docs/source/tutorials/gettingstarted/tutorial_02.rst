.. _installing_websauna:

===================
Installing Websauna
===================

.. contents:: :local:

Preface
=======

Websauna is a Python package and requires a number of dependencies.

External dependencies
=====================

To run Websauna on your local computer you need

* :term:`PostgreSQL` 9.4 or newer

* :term:`Redis`

* :term:`Python` 3.5 or newer

* `libxml2 <http://www.xmlsoft.org/>`_

Installing dependencies on OSX
------------------------------

`Install XCode <https://developer.apple.com/xcode/download/>`_.

`Install Homebrew <http://brew.sh/>`_.

Install Python 3.5, Redis, PostgreSQL:

.. code-block:: console

    brew install postgresql redis python3 libxml2

Make sure PostgreSQL and Redis are started on your computer:

.. code-block:: console

    brew services start postgresql
    brew services start redis

Then you can see them:

.. code-block:: console

    brew services list

    # ...
    Name         Status  User Plist
    postgresql   started moo  /Users/mikko/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
    redis        started moo  /Users/mikko/Library/LaunchAgents/homebrew.mxcl.redis.plist

Make sure ``python3`` command points to Python 3.5:

.. code-block:: console

    python3.5 --version

Should give you::

    Python 3.5.0

If it shows a different version use ``brew switch`` command to upgrade

.. code-block:: console

    brew upgrade python3
    brew link python3 --overwrite

Installing dependencies on Ubuntu 14.04
---------------------------------------

The following install commands apply for Ubuntu 14.04 and 14.04 only (for example newer Ubuntus come with up-to-date PostgreSQL).

Install the packages with following command:

.. code-block:: console

    sudo apt install \
        git \
        build-essential \
        libfreetype6-dev \
        libncurses5-dev \
        libxml2-dev \
        libxslt1-dev \
        libjpeg-dev \
        libpng12-dev \
        libffi-dev \
        gettext \
        python-virtualenv \
        python-software-properties

Install Python 3.5

.. code-block:: console

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get update
    sudo apt -y install python3.5 python3.5-dev

Install Redis

.. code-block:: console

    sudo apt install redis-server

Install PostgreSQL

.. code-block:: console

    # http://technobytz.com/how-to-install-postgresql-9-4-in-ubuntu-linux-mint.html
    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install postgresql-9.4 libpq-dev


Installing dependencies on openSUSE 13.2 and Leap 42.1
------------------------------------------------------

Install Redis

.. code-block:: console

    # as root
    zypper install redis
    cp -a /etc/redis/default.conf.example /etc/redis/default.conf
    systemctl enable redis.service
    systemctl start redis.service

For 13.2 we need an additional repository for PostgreSQL 9.4. If you have an older PostgreSQL running already, please check /usr/share/doc/packages/postgresql94/README.SUSE for database migration.

.. code-block:: console

    zypper ar -f http://download.opensuse.org/repositories/server:/database:/postgresql/openSUSE_13.2/server:database:postgresql.repo

Install PostgreSQL 9.4

.. code-block:: console

    zypper install postgresql94-server postgresql94-devel postgresql94-contrib
    systemctl enable postgresql.service
    systemctl start postgresql.service

Installing Websauna Python package
==================================

In this guide we create `a Python virtual environment <https://packaging.python.org/en/latest/installing/#creating-virtual-environments>`_ where Websauna package and its Python package dependencies are installed.

Create ``myproject`` folder and enter into it:

.. code-block:: console

    mkdir myproject
    cd myproject

Then create a virtual environment where installed Python packages will be located:

.. code-block:: console

    # This creates venv folder with Python environment for your project
    python3.5 -m venv venv

    # This will activate the environment for your current shell session
    source venv/bin/activate

    pip install "websauna[celery,utils,notebook]"

Alternatively, in the case you want to leave on a bleeding edge, you can install the latest master from GitHub. This is recommended for experienced Python developers only:

.. code-block:: console

    # Install GitHub development version of Websauna
    pip install -e "git+https://github.com/websauna/websauna.git@master#egg=websauna[celery,utils,notebook]"
