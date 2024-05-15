#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(f"count:{cache.store.__qualname__}"))  # Output: b'1'

cache.store(b"second")
cache.store(b"third")
print(cache.get(f"count:{cache.store.__qualname__}")) 