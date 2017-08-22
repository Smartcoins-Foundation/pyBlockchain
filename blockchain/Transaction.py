#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import hashlib
import random


# Transaction
class Transaction(object):
    """
    A transaction
    """

    # Constructor
    def __init__(self, previous_transaction_id, count, sign, dest):
        """
        Constructor
        :param previous_transaction_id: The previous transaction's ID
        :param count: Sum to transfer
        :param sign: Signature by the source
        :param dest: Public key of the destination
        """
        # Properties
        self._transaction_id = random.getrandbits(128)
        self._previous_transaction_id = previous_transaction_id
        self._count = count
        self._signature = sign
        self._destination = dest
    # end __init__

    #############################################
    # Public
    #############################################

    # Hash code
    def hash(self):
        """
        Hash code
        :return:
        """
        # SHA 256 hashing
        m = hashlib.sha256()

        # Add transaction id
        m.update(self._transaction_id)

        # Add previous transaction id
        m.update(self._previous_transaction_id)

        # Add count
        m.update(self._count)

        # Signature
        m.update(self._signature)

        # Add destination
        m.update(self._destination)

        return m.digest()
    # end hash

    # Serialize transaction
    def serialize(self):
        """
        Serialize transaction
        :return:
        """
        data = dict()

        # Transaction ID
        data['id'] = self._transaction_id

        # Previous transaction id
        data['previous'] = self._previous_transaction_id

        # Count
        data['count'] = self._count

        # Signature
        data['sign'] = str(self._signature)

        # Destination
        data['dest'] = str(self._destination)

        return data
    # end serialize

    #############################################
    # Override
    #############################################

# end Transaction
