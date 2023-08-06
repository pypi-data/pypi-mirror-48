# -*- coding: utf-8 -*-
from . import credentials as credentials_impl, table, scheme, pool


class DriverConfig(object):
    __slots__ = ('endpoint', 'database', 'ca_cert', 'channel_options', 'credentials', 'use_all_nodes')

    def __init__(
            self, endpoint, database=None, ca_cert=None, auth_token=None,
            channel_options=None, credentials=None, use_all_nodes=False):
        """
        A driver config to initialize a driver instance
        :param endpoint: A endpoint specified in pattern host:port to be used for initial
        channel initialization and for YDB endpoint discovery mechanism
        :param database: A name of the database
        :param ca_cert: A CA certificate when SSL should be used
        :param auth_token: A authentication token
        :param credentials: An instance of AbstractCredentials
        BVzz:param use_all_nodes: A balancing policy that forces to use all available nodes.
        """
        self.endpoint = endpoint
        self.database = database
        self.ca_cert = ca_cert
        self.channel_options = channel_options
        if auth_token is not None:
            credentials = credentials_impl.AuthTokenCredentials(auth_token)
        self.credentials = credentials
        self.use_all_nodes = use_all_nodes

    def set_database(self, database):
        self.database = database
        return self


ConnectionParams = DriverConfig


class Driver(pool.ConnectionPool):
    __slots__ = ('scheme_client', 'table_client')

    def __init__(self, driver_config):
        """
        Constructs a driver instance to be used in table and scheme clients.
        It encapsulates endpoints discovery mechanism and provides ability to execute RPCs
        on discovered endpoints

        :param driver_config: A driver config
        """
        super(Driver, self).__init__(driver_config)
        self.scheme_client = scheme.SchemeClient(self)
        self.table_client = table.TableClient(self)
