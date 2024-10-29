#!/usr/bin/env python3
"""A python script that provides some stats about Nginx logs
stored in mongodb
"""
from pymongo import MongoClient
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]
CLIENT = MongoClient("mongodb://127.0.0.1:27017/logs")


def main():
    """
    Main driver of the program. Provides some stats about nginx logs
    stored in mongodb
    """
    nginx_logs = CLIENT.get_database().get_collection("nginx")

    total_logs = nginx_logs.count_documents({})
    stats = [*get_stats(nginx_logs)]

    print("{} logs".format(total_logs))
    print("Methods: ")
    for method in METHODS:
        print("\tmethod {}: {}".format(method, total_request(method, stats)))
    print("{} status check".format(status_check(nginx_logs).get("checks")))


def total_request(method, stats):
    """
    Calculates the total request for a method
    """
    total = 0
    stat = find(stats, lambda stat: stat.get('_id') == method)
    if stat is None:
        return 0
    return stat['total_request']


def find(arr, func):
    """
    Checks if an element in the list, l, is true when evaluated
    by func
    """
    for element in arr:
        if func(element):
            return element
    return None


def get_stats(nginx_logs):
    """gets the stats of the nginx logs
    """
    return nginx_logs.aggregate([
        {
            "$match": {
                "method": {"$in": METHODS}
            }
        },
        {
            "$group": {
                "_id": "$method",
                "total_request": {"$sum": 1}
            }
        }
    ])


def status_check(nginx_logs):
    """gets the total number of status checks request from the log
    """
    return [*nginx_logs.aggregate([
        {
            "$match": {
                "method": "GET",
                "path": "/status"
            }
        },
        {
            "$group": {
                "_id": "$method",
                "checks": {"$sum": 1}
            }
        }
    ])][0]


if __name__ == "__main__":
    main()
