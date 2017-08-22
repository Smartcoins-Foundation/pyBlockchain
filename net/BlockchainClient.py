#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import socket
import json


# A Blockchain client
class BlockchainClient(object):
    """
    A Blockchain client
    """

    # Constructor
    def __init__(self, host, port):
        """
        Constructor
        :param host: Hostname to listen to
        :param port: Source port
        """
        # Properties
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # end __init__

    ##################################################
    # Public
    ##################################################

    # Connect
    def connect(self):
        """
        Connect
        :return:
        """
        # connect to server
        self._socket.connect((self._host, self._port))
    # end connect

    # Send a transaction
    def send_transaction(self, transaction):
        """
        Send a transaction
        :param transaction:
        :return:
        """
        self._socket.sendall(json.dumps({'type': "transaction", 'object': transaction.serialize()}))
    # end send_transaction

    # Close connection
    def close(self):
        """
        Close connection
        :return:
        """
        self._socket.close()
    # end close

# end BlockchainClient
