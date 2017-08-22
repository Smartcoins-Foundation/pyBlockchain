#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import SocketServer
from server.BlockchainServer import BlockchainServer


if __name__ == "__main__":

    # Config
    HOST, PORT = "localhost", 9999

    # Instantiate the server, and bind to port 9999
    blockchain_server = SocketServer.TCPServer((HOST, PORT), BlockchainServer)

    # Activate the server
    blockchain_server.serve_forever()

# end if
