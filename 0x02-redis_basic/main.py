#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

key_first = cache.store(b"first")
print(cache.get(key_first))  # Retrieve the data associated with the key

# Store more data
key_second = cache.store(b"second")
key_third = cache.store(b"third")

# Retrieve data using the correct keys
print(cache.get(key_second))  # Retrieve the data associated with the key generated for "second"
print(cache.get(key_third))   