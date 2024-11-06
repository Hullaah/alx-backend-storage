#!/usr/bin/env python3
"""implements a web cache and tracker
"""
import redis
import requests

_redis = redis.Redis()

def get_page(url: str) -> str:
    resu
    res = requests.get(url)
