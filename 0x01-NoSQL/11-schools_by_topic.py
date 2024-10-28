#!/usr/bin/env python3
"""A script that returns the list of schools having a specific topic
"""
from pymongo.collection import Collection
from typing import List


def schools_by_topic(mongo_collection: Collection, topic: str) -> List:
    return [*mongo_collection.find({"topics": {"$in": [topic]}})]
