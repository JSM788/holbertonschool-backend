#!/usr/bin/env python3
"""Defining the class BasicCache in 0-basic_cache file"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Upgrade to BaseCaching"""

    def put(self, key, item):
        """Add a key and an item in cache_data"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item based on a key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
