#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import SocketServer


# A Blockchain server
class BlockchainServer(SocketServer.BaseRequestHandler):
    """
    A Blockchain server
    """

    # Handle
    def handle(self):
        """
        Handle the request
        :return:
        """
        data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        self.request.sendall(data.upper())
    # end handle

# end BlockchainServer
