#!/usr/bin/env python3
"""Defining the FIFOCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This class removes the first value entered in cache_data"""

    def put(self, key, item):
        """Upgrade to BaseCaching"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            sorted_data = sorted(self.cache_data)
            removed_key = sorted_data[0]
            self.cache_data.pop(removed_key)
            print(f"DISCARD: {removed_key}")

    def get(self, key):
        """Get an item based on a key"""
        if key is None:
            return None
        # get() returns None if it doesn't find the key
        return self.cache_data.get(key)
