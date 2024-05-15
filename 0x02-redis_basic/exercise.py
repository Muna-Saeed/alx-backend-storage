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
    #!/usr/bin/env python3
"""
Module for basic Redis operations.
"""

import redis
import uuid
from typing import Union, Callable, Optional

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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve the data from Redis and optionally apply a conversion function.

        :param key: The key to retrieve from Redis.
        :param fn: Optional callable to convert the data back to the desired format.
        :return: The data from Redis, possibly converted by the callable.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the data from Redis as a UTF-8 string.

        :param key: The key to retrieve from Redis.
        :return: The data as a UTF-8 string, or None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the data from Redis as an integer.

        :param key: The key to retrieve from Redis.
        :return: The data as an integer, or None if the key does not exist.
        """
        return self.get(key, lambda d: int(d))
