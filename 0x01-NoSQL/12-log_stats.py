#!/usr/bin/env python3
"""A python script that provides some stats about Nginx logs
stored in mongodb
"""
from pymongo import MongoClient
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]
CLIENT = MongoClient("mongodb://127.0.0.1:27017/logs")


def main():
    nginx_logs = CLIENT.get_database().get_collection("nginx")

    total_logs = nginx_logs.count_documents({})
    stats = nginx_logs.aggregate([
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
    stats = [*stats]

    print("{} logs".format(total_logs))
    print("Methods: ")
    for method in METHODS:
        print("\tmethod {}: {}".format(method, total_request(method, stats)))


def total_request(method, stats):
    total = 0
    stat = find(stats, lambda stat: stat.get('_id') == method)
    if stat is None:
        return 0
    return stat['total_request']


def find(l, func):
    for element in l:
        if func(element):
            return element
    return None


if __name__ == "__main__":
    main()
