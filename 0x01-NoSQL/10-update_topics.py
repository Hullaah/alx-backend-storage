#!/usr/bin/env python3
"""Changes all topics of a school document based on the name
"""
from pymongo.collection import Collection
from typing import List


def update_topics(mongo_collection: Collection, name: str, topics: List[str]):
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
