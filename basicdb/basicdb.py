# Copyright (c) 2016 John Tye Bennett
# See LICENSE for details

import logging
import re
from contextlib import contextmanager

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL


class Database(object):
    logger = logging.getLogger('database')

    def __init__(self, **config):
        self.connection_details = {
            'drivername': config.get('drivername'),
            'host': config.get('host'),
            'port': config.get('port'),
            'database': config.get('database'),
            'username': config.get('username'),
            'password': config.get('password'),
        }
        self.engine_details = {
            'echo': config.get('echo'),
        }
        self.initialized = False

    def masked_url(self):
        return re.sub(r'://([^:]+):[^@]+', r'://\1:******', str(self.url))

    def initialize(self):
        if not self.initialized:
            self.url = URL(**self.connection_details)
            self.engine = create_engine(self.url, **self.engine_details)
            self.create_session = sessionmaker(bind=self.engine)
            self.initialized = True
            self.logger.debug('Database initialize with url {}'.format(
                self.masked_url()))
        return self

    def close(self):
        self.engine.dispose()
        self.initialized = False
        return self

    def execute(self, sql, params={}):
        self.initialize()
        return self.engine.execute(text(sql), params)

    @contextmanager
    def scoped_session(self):
        self.initialize()
        session = self.create_session()
        try:
            yield session
        finally:
            session.close()
