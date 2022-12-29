#!/usr/bin/env python3
"""Defining the LIFOCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class removes the last value entered in cache_data"""

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Upgrade to BaseCaching"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.keys[-1]]
            print(f"DISCARD: {self.keys[-1]}")
        self.keys.append(key)

    def get(self, key):
        """Get an item based on a key"""
        if key is None:
            return None
        # get() returns None if it doesn't find the key
        return self.cache_data.get(key)
