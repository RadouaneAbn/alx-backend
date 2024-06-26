#!/usr/bin/env python3
""" 2-lifo_cache """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        """
        Initializes the LIFOCache instance.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Adds a key-value pair to the cache following the Last In,
        First Out (LIFO) principle.
        If the cache is full and the key is not already present,
        it removes the most recently added item before adding the
        new key-value pair.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.cache_data:
            self.cache_data.pop(self.last_key)
            print("DISCARD:", self.last_key)
        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """
        Retrieves a value from the cache by key.

        Args:
            key: The key whose value needs to be retrieved.

        Returns:
            The value associated with the key if it exists, None otherwise.
        """
        return self.cache_data.get(key, None)
