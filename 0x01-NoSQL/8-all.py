#!/usr/bin/env python3
"""
A python script that lists all documents in a collection
"""


def list_all(mongo_collection):
    """Lists all documents in a collection
    """
    return [*mongo_collection.find()]
