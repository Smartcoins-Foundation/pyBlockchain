#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import socket
import sys
import argparse
from net.BlockchainClient import BlockchainClient
from blockchain.Transaction import Transaction


# Main function
if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="pyBlockchain - Client")

    # Argument
    parser.add_argument("--host", type=str, help="Hostname address to listen  to", required=True)
    parser.add_argument("--port", type=int, help="Port number to listen to", default=3818)
    args = parser.parse_args()

    # Client to blockchain server
    client = BlockchainClient(args.host, args.port)

    # Connection
    client.connect()

    # New transaction
    trans = Transaction(previous_transaction_id=-1, count=200, sign="", dest="")

    # Send
    client.send_transaction(trans)

    # Close
    client.close()
# end if
