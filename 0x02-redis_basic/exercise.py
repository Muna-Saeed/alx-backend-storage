#!/usr/bin/env python3
"""
Module for basic Redis operations.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for interacting with Redis.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis with a random key and return the key.

        :param data: Data to store in Redis. Can be str, bytes, int, or float.
        :return: The generated random key as a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
