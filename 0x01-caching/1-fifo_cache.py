#!/usr/bin/env python3
""" 1-fifo_cache module """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class is a caching system that follows the First In First Out
    (FIFO) principle.
    It inherits from BaseCaching and allows storing and retrieving
    key-value pairs with a limit on the number of items. When the cache
    exceeds the limit, the oldest item is removed.

    Methods:
        __init__(self): Initializes the FIFOCache instance.
        put(self, key, item): Adds a key-value pair to the cache,
        removing the oldest item if necessary.
        get(self, key): Retrieves a value from the cache by key.
    """
    def __init__(self):
        """
        Initializes the FIFOCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.
        If the cache exceeds the maximum limit,
        the oldest item (first inserted) is removed.

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
            poped_item = next(iter(self.cache_data))
            self.cache_data.pop(poped_item)
            print("DISCARD:", poped_item)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a value from the cache by key.

        Args:
            key: The key whose value needs to be retrieved.

        Returns:
            The value associated with the key if it exists, None otherwise.
        """
        return self.cache_data.get(key, None)
