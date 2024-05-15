#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    print(f"Storing value: {value}")
    key = cache.store(value)
    print(f"Retrieved key: {key}")
    retrieved_value = cache.get(key, fn=fn)
    print(f"Retrieved value: {retrieved_value}")
    assert retrieved_value == value
