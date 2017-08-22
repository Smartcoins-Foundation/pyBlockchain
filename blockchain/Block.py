#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import hashlib


# Block
class Block(object):
    """
    A block of transaction
    """

    # Properties
    _previous_block = None

    # Constructor
    def __int__(self):
        """
        Constructor
        :return:
        """
        # Properties
        self._previous_block = None
        self._transactions = list()
    # end __init__

    ###############################################
    # Public
    ###############################################

    # Set the previous block
    def set_previous_block(self, previous_block):
        """
        Set the previous block
        :param previous_block:
        :return:
        """
        self._previous_block = previous_block
    # end set_previous_block

    # Add a transaction
    def add_transaction(self, transaction):
        """
        Add a transaction
        :param transaction:
        :return:
        """
        self._transactions.append(transaction)
    # end add_transaction

    # Get the hash code
    def hash(self):
        """
        Get the hash code
        :return:
        """
        # SHA 256 hashing
        m = hashlib.sha256()

        # Add previous block
        if self._previous_block is not None:
            m.update(self._previous_block.hash())
        # end if

        # Add transactions
        for transaction in self._transactions:
            m.update(transaction.hash())
        # end for

        return m.digest()
    # end hash

    # Serialize the object
    def serialize(self):
        """
        Serialize the object
        :return:
        """
        pass
    # end serialize

# end Block
