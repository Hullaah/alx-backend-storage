#!/usr/bin/env python3
"""The script contains the Cache class
"""
import redis
from functools import wraps
from typing import Union, Callable, Optional
from uuid import uuid4


def call_history(method: Callable) -> Callable:
    """Stores the call history (history of inputs and outputs)
    of calls to a particular function

    Args:
        method: method to store call history of

    Returns:
        the function unchanged
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        self, *args = args
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        result = method(*args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", result)
        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Counts the number of times a function is called

    Args:
        method: function to count

    Returns:
        the function unchanged
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        self, *args = args
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ creates a cache
    """

    def __init__(self) -> None:
        """initializes the cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data in cache

        Args:
            data: data to be stored in the cache

        Returns:
            The key used to store the data
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """gets a value from the cache

        Args:
            key: key to use in getting value from the cache
            fn: optional function to use to convert the gotten
                value from the cache

        Returns:
            The value gotten from the cache
        """
        value = self._redis.get(key)
        return value if fn is None else fn(value)
