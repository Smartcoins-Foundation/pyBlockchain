#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import argparse
import logging

from net.BlockchainServer import BlockchainServer

# Main function
if __name__ == "__main__":
    # Config
    HOST, PORT = "localhost", 9999

    # Argument parser
    parser = argparse.ArgumentParser(description="pyBlockchain - Server")

    # Argument
    parser.add_argument("--host", type=str, help="Hostname address to listen  to", required=True)
    parser.add_argument("--port", type=int, help="Port number to listen to", default=3818)
    args = parser.parse_args()

    # Logging
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(name)s-%(levelname)s : %(message)s")

    # Instantiate the server, and bind to port 9999
    blockchain_server = BlockchainServer(args.host, args.port)

    # Starting server
    logging.info(u"Starting server")
    blockchain_server.start()

    # Wait the end
    try:
        while blockchain_server.isAlive():
            blockchain_server.join(5)
        # end while
    except (KeyboardInterrupt, SystemExit):
        logging.info(u"Signal received, exiting")
        blockchain_server.stop()
    # end try
# end if
