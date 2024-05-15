#!/usr/bin/env python3
"""
Cache module
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """store an instance of the Redis and flush the instance using flushdb"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes a data argument and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    def get(self, key: str, fn: Callable = None) ->  Union[bytes, None]:
        """ used to convert the data back to the desired format """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value
    def get_str(self, key: str) -> Optional[str]:
        """parametrizes Cache.get with the correct conversion function"""
        return self.get(key, lambda x: x.decode('utf-8') if x else None)

    def get_int(self, key: int) -> Optional[int]:
        """parametrizes Cache.get with the correct conversion function"""
        return self.get(key, fn=int)

        

