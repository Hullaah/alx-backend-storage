#!/usr/bin/env python3
"""
A python script that lists all documents in a collection
"""
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List:
    """Lists all documents in aa  collection
    """
    return [*mongo_collection.find()]
