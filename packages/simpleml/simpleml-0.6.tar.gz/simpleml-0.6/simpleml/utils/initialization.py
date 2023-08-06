'''
Util module to initialize SimpleML and configure
database management
'''

__author__ = 'Elisha Yadgaran'


# Import table models to register in DeclaritiveBase
from simpleml.persistables.base_persistable import Persistable
import simpleml.datasets.base_dataset
import simpleml.pipelines.base_pipeline
import simpleml.models.base_model
import simpleml.metrics.base_metric
from simpleml.persistables.dataset_storage import DatasetStorage
from simpleml.persistables.binary_blob import BinaryBlob
from simpleml.persistables.serializing import custom_dumps, custom_loads
from simpleml.utils.errors import SimpleMLError
from simpleml.utils.configuration import CONFIG

from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine.url import URL
from alembic import command
from alembic.config import Config
from alembic.migration import MigrationContext
from alembic.script import ScriptDirectory
from os.path import realpath, dirname, join
import os
import logging

LOGGER = logging.getLogger(__name__)


# Database Defaults
DATABASE_NAME = os.getenv('SIMPLEML_DATABASE_NAME', 'SimpleML')
DATABASE_USERNAME = os.getenv('SIMPLEML_DATABASE_USERNAME', 'simpleml')
DATABASE_PASSWORD = os.getenv('SIMPLEML_DATABASE_PASSWORD', 'simpleml')
DATABASE_HOST = os.getenv('SIMPLEML_DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('SIMPLEML_DATABASE_PORT', 5432)
DATABASE_DRIVERNAME = os.getenv('SIMPLEML_DATABASE_DRIVERNAME', 'postgresql')
DATABASE_CONF = os.getenv('SIMPLEML_DATABASE_CONF', None)
DATABASE_URI = os.getenv('SIMPLEML_DATABASE_URI', None)


class BaseDatabase(URL):
    '''
    Base Database class to configure db connection
    Does not assume schema tracking or any other validation
    '''
    def __init__(self, configuration_section=DATABASE_CONF, uri=DATABASE_URI, database=DATABASE_NAME,
                 username=DATABASE_USERNAME, password=DATABASE_PASSWORD, drivername=DATABASE_DRIVERNAME,
                 host=DATABASE_HOST, port=DATABASE_PORT, **kwargs):
        if configuration_section is not None:
            # Default to credentials in config file
            credentials = dict(CONFIG[configuration_section])
            credentials.update(kwargs)
            super(BaseDatabase, self).__init__(**credentials)
        else:
            if uri is not None:
                # Overwrite all the other parameters and inject URI directly into the engine
                LOGGER.info('Skipping parameters and using passed URI')
                self.uri = uri
                LOGGER.info('Inputting dummy parameters to force initialization - still using URI in engine!')

            super(BaseDatabase, self).__init__(
                drivername=drivername,
                username=username,
                password=password,
                host=host,
                port=port,
                database=database,
                **kwargs
            )

    @property
    def engine(self):
        if hasattr(self, 'uri') and self.uri is not None:
            uri = self.uri
        else:
            uri = self
        # Custom serializer/deserializer not supported by all drivers
        # Definitely works for:
        # - Postgres
        # Definitely does not work for:
        # - SQLite
        return create_engine(uri,
                             json_serializer=custom_dumps,
                             json_deserializer=custom_loads,
                             pool_recycle=300)

    def create_tables(self, base, drop_tables=False, ignore_errors=False):
        '''
        Creates database tables (and potentially drops existing ones).
        Assumes to be running under a sufficiently privileged user

        :param drop_tables: Whether or not to drop the existing tables first.
        :return: None
        '''
        try:
            if drop_tables:
                base.metadata.drop_all()

            base.metadata.create_all()

        except ProgrammingError as e:  # Permission errors
            if ignore_errors:
                LOGGER.debug(e)
            else:
                raise(e)

    def _initialize(self, base, create_tables=False, **kwargs):
        '''
        Initialization method to set up database connection and inject
        session manager

        :param create_tables: Bool, whether to create tables in database
        :param drop_tables: Bool, whether to drop existing tables in database
        :return: None
        '''
        engine = self.engine
        session = scoped_session(sessionmaker(autocommit=True,
                                              autoflush=False,
                                              bind=engine))
        base.metadata.bind = engine
        base.query = session.query_property()

        if create_tables:
            self.create_tables(base, **kwargs)

        base.set_session(session)

    def initialize(self, base_list, **kwargs):
        '''
        Initialization method to set up database connection and inject
        session manager

        Raises a SimpleML error if database schema is not up to date

        :param drop_tables: Bool, whether to drop existing tables in database
        :param upgrade: Bool, whether to run an upgrade migration after establishing a connection
        :return: None
        '''
        for base in base_list:
            self._initialize(base, **kwargs)


class AlembicDatabase(BaseDatabase):
    '''
    Base database class to manage dbs with schema tracking. Includes alembic
    config references
    '''
    def __init__(self, alembic_filepath, script_location='migrations', *args, **kwargs):
        self.alembic_filepath = alembic_filepath
        self.script_location = script_location
        super(AlembicDatabase, self).__init__(*args, **kwargs)

    @property
    def alembic_config(self):
        if not hasattr(self, '_alembic_config'):
            # load the Alembic configuration
            self._alembic_config = Config(self.alembic_filepath)
            # For some reason, alembic doesnt use a relative path from the ini
            # and cannot find the migration folder without the full path
            self._alembic_config.set_main_option('script_location', join(dirname(self.alembic_filepath), self.script_location))
        return self._alembic_config

    def create_tables(self, base, drop_tables=False, ignore_errors=False):
        '''
        Creates database tables (and potentially drops existing ones).
        Assumes to be running under a sufficiently privileged user

        :param drop_tables: Whether or not to drop the existing tables first.
        :return: None
        '''
        try:
            if drop_tables:
                base.metadata.drop_all()
                # downgrade the version table, "stamping" it with the base rev
                command.stamp(self.alembic_config, "base")

            base.metadata.create_all()
            # generate/upgrade the version table, "stamping" it with the most recent rev
            command.stamp(self.alembic_config, "head")

        except ProgrammingError as e:  # Permission errors
            if ignore_errors:
                LOGGER.debug(e)
            else:
                raise(e)

    def upgrade(self, revision='head'):
        '''
        Proxy Method to invoke alembic upgrade command to specified revision
        '''
        command.upgrade(self.alembic_config, revision)

    def downgrade(self, revision):
        '''
        Proxy Method to invoke alembic downgrade command to specified revision
        '''
        command.downgrade(self.alembic_config, revision)

    def validate_schema_version(self):
        '''
        Check that the newly initialized database is up-to-date
        Raises an error otherwise (ahead of any table model mismatches later)
        '''
        # Establish a context to access db values
        context = MigrationContext.configure(self.engine.connect())
        current_revision = context.get_current_revision()

        # Read local config file to find the current "head" revision
        # config = Config()
        # config.set_main_option("script_location",
        #                        join(dirname(dirname(dirname(realpath(__file__)))), "migrations"))
        script = ScriptDirectory.from_config(self.alembic_config)
        head_revision = script.get_current_head()

        if current_revision != head_revision:
            raise SimpleMLError('''Attempting to connect to an outdated schema.
                                Set the parameter `upgrade=True` in the initialize method
                                or manually execute `alembic upgrade head` in a shell''')

    def initialize(self, base_list, upgrade=False, **kwargs):
        '''
        Initialization method to set up database connection and inject
        session manager

        Raises a SimpleML error if database schema is not up to date

        :param drop_tables: Bool, whether to drop existing tables in database
        :param upgrade: Bool, whether to run an upgrade migration after establishing a connection
        :return: None
        '''
        # Standard initialization
        super(AlembicDatabase, self).initialize(base_list, **kwargs)

        # Upgrade schema if necessary
        if upgrade:
            self.upgrade()

        # Assert current db schema is up-to-date
        self.validate_schema_version()


class Database(AlembicDatabase):
    '''
    SimpleML specific configuration to interact with the database
    '''
    def __init__(self, *args, **kwargs):
        root_path = dirname(dirname(dirname(realpath(__file__))))
        alembic_filepath = join(root_path, 'alembic.ini')
        script_location = 'simpleml/migrations'
        super(Database, self).__init__(
            alembic_filepath=alembic_filepath, script_location=script_location, *args, **kwargs)

    def initialize(self, base_list=None, **kwargs):
        '''
        Initialization method to set up database connection and inject
        session manager

        Raises a SimpleML error if database schema is not up to date

        :param drop_tables: Bool, whether to drop existing tables in database
        :param upgrade: Bool, whether to run an upgrade migration after establishing a connection
        :return: None
        '''
        if base_list is None:  # Use defaults in project
            base_list = [Persistable]

        super(Database, self).initialize(base_list, **kwargs)
