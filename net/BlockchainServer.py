#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import socket
import logging
import time
import json
from threading import Thread


# A Blockchain server
class BlockchainServer(Thread):
    """
    A Blockchain server
    """

    # Constructor
    def __init__(self, host, port, queue_size=5):
        """
        Constructor
        :param host: Hostname to listen to
        :param port: Source port
        :param queue_size: Queue size
        """
        # Thread
        Thread.__init__(self)
        self.daemon = True

        # Properties
        self._running = False
        self._host = host
        self._port = port
        self._queue_size = queue_size
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # end __init__

    ##################################################
    # Public
    ##################################################

    # Run server
    def run(self):
        """
        Start the server
        :return:
        """
        # Bind the port
        logging.info(u"Bind the port ({}:{})".format(self._host, self._port))
        self._server_socket.bind((self._host, self._port))

        # Listening
        logging.info(u"Listening to {}:{}".format(self._host, self._port))
        self._server_socket.listen(self._queue_size)

        # Running
        logging.info(u"Server running...")
        self._running = True

        # Main loop
        while self._running:
            # Establish a connection
            client_socket, addr = self._server_socket.accept()

            # Log connection
            logging.info(u"Connection from {}".format(addr))

            # Get data
            data = client_socket.recv(2048)

            # Transform to JSON
            try:
                json_data = json.loads(data)
                print(json_data)
                client_socket.close()
            except ValueError as e:
                client_socket.sendall(json.dumps({'code': 400, 'message': str(e)}))
                client_socket.close()
                pass
            # end try
        # end while
    # end start

    # Stop the server
    def stop(self):
        """
        Stop the server
        :return:
        """
        logging.info(u"Stopping server...")
        self._running = False
    # end stop

# end BlockchainServer
