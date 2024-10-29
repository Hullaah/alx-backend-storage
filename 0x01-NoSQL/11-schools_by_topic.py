#!/usr/bin/env python3
"""A script that returns the list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a specific topic"""
    return [*mongo_collection.find({"topics": {"$in": [topic]}})]
