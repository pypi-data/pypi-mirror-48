# Standard Library
import sys
from codecs import open
from os import path

from setuptools import find_packages
from setuptools import setup


assert sys.version_info >= (3, 5, 2), "Websauna needs Python 3.5.2 or newer, you have {version}".format(version=sys.version_info)

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='websauna',
    namespace_packages=["websauna"],
    version='1.0a13',
    description=long_description.split("\n")[0],
    long_description=long_description,
    url='https://websauna.org',
    author='Mikko Ohtamaa',
    author_email='mikko@opensourcehacker.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    keywords='sqlalchemy postgresql pyramid pytest websauna',
    packages=find_packages(exclude=['docs']),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.5.2',
    install_requires=[
        # Pyramid dependencies
        'pyramid>=1.10,<2.0.0',
        'transaction>=2.4.0',
        'waitress',
        'pyramid_redis_sessions',
        'pyramid-layout',
        "deform>=2.0.4",
        "pyramid_debugtoolbar",
        "pyramid_jinja2",

        # Time handling
        "arrow",
        "pytz>=2019.1",

        # SQLAlchemy and database support
        "alembic",
        "colanderalchemy",
        "psycopg2",
        "pyramid_retry",
        "pyramid_tm",
        "sqlalchemy",
        "sqlalchemy-utils",
        "zope.sqlalchemy",

        # User management
        "argon2_cffi",
        "authomatic",

        # Email
        'pyramid-mailer',
        'premailer',

        # Console logging
        "rainbow_logging_handler",

        # Misc
        "python-slugify",  # ASCII slug generation

        # Redis
        "redis>=3.2",
    ],

    extras_require={
        # Dependencies needed to build and release Websauna
        'dev': [
            'setuptools_git',
            'zest.releaser[recommended]',
        ],
        'docs': [
            'ruamel.yaml',
            'sphinx-autodoc-typehints',
            'sphinx>=1.6.1',
            'sphinx_rtd_theme',
            'sphinxcontrib-zopeext',
        ],
        'test': [
            'codecov',
            'cookiecutter',
            'coverage',
            'flake8',
            'flaky',
            'isort',
            'pytest-cov',
            'pytest-runner',
            'pytest-splinter',
            'pytest-timeout',
            'pytest-services',
            'pytest',
            'webtest',
        ],
        "notebook": [
            "pyramid_notebook>=0.3.0",
        ],
        # Command line utilities and like that are needed to make development / production environment friendly
        'utils': ['pgcli>=2'],
        # Using celery based async tasks
        'celery': ['celery[redis]>=4.3.0,<5.0.0']
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'ws-sync-db=websauna.system.devop.scripts.syncdb:main',
            'ws-db-shell=websauna.system.devop.scripts.dbshell:main',
            'ws-shell=websauna.system.devop.scripts.shell:main',
            'ws-tweens=websauna.system.devop.scripts.tweens:main',
            'ws-alembic=websauna.system.devop.scripts.alembic:main',
            'ws-dump-db=websauna.system.devop.scripts.dumpdb:main',
            'ws-create-user=websauna.system.devop.scripts.createuser:main',
            'ws-celery=websauna.system.task.celeryloader:main',
            'ws-proutes=websauna.system.devop.scripts.proutes:main',
            'ws-pserve=websauna.system.devop.scripts.pserve:main',
            'ws-create-table=websauna.system.devop.scripts.createtable:main',
            'ws-sanity-check=websauna.system.devop.scripts.sanitycheck:main',
            'ws-collect-static=websauna.system.devop.scripts.collectstatic:main',
            'ws-settings=websauna.system.devop.scripts.settings:main',
        ],

        'paste.app_factory': [
            'main=websauna.system:main',
            # Scheduler automated test suite entry point with some extra configured taskss
            'task_test=websauna.tests.task.demotasks:main',
            'tutorial_test=websauna.tests.crud.tutorial:main',
        ],

        'plaster.loader_factory': [
            'ws=websauna.utils.config.loader:Loader',
        ],

        'plaster.wsgi_loader_factory': [
            'ws=websauna.utils.config.loader:Loader',
        ],
    },
)
