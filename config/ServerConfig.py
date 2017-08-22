#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
from templates.singleton import singleton


# Server configuration
@singleton
class ServerConfig(object):
    """
    Server configuration
    """

    # Constructor
    def __init__(self, data):
        """
        Constructor
        :param data:
        """
        self._config_data = data
    # end __init__

    #############################################
    # Public
    #############################################

    # Get server address
    def get_server_address(self):
        """
        Get server address
        :return:
        """
        pass
    # end get_server_address

# end ServerConfig
