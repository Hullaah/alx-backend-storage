#!/usr/bin/env python3
"""
A python script that inserts a new document in a collection based on kwargs
"""
from pymongo.collection import Collection
from typing import Mapping


def insert_school(mongo_collection: Collection, **kwargs: Mapping) -> str:
    """Inserts a new document in a collection based on kwargs
    """
    return mongo_collection.insert_one(kwargs).inserted_id
