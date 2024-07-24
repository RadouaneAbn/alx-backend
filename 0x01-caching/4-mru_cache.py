#!/usr/bin/env python3
""" MRUCache module """
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that follows the Most Recently Used (MRU) principle.
    Inherits from BaseCaching.
    """
    def __init__(self):
        """
        Initializes the MRUCache instance.
        """
        super().__init__()
        self.item_list = []

    def put(self, key, item):
        """
        Adds a key-value pair to the cache. If the cache is full, removes
        the most recently used item.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.item_list:
            self.item_list.pop(self.item_list.index(key))
        elif len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.item_list:
            last_used_item = self.item_list.pop(-1)
            print("DISCARD:", last_used_item)
            self.cache_data.pop(last_used_item)
        self.item_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a value from the cache by key.

        Args:
            key: The key whose value needs to be retrieved.

        Returns:
            The value associated with the key if it exists, None otherwise.
        """
        if key and key in self.item_list:
            last_item = self.item_list.pop(self.item_list.index(key))
            self.item_list.append(last_item)
        return self.cache_data.get(key, None)
