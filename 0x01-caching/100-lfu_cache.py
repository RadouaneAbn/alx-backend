#!/usr/bin/env python3
""" 100-lfu_cache.py """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """
        Initializes the MRUCache instance.
        """
        super().__init__()
        self.item_dict = {}

    @staticmethod
    def get_least_frequent(dict_lfu):
        """
        Returns the key with the least frequency from the frequency dictionary.
        """
        sorted_tuple = sorted(dict_lfu.items(),
                              key=lambda item: item[1])
        return sorted_tuple[0][0]

    def put(self, key, item):
        """
        Adds a key-value pair to the cache. If the cache is full, removes
        the least frequently used item.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.item_dict:
            self.item_dict[key] += 1
        elif len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.item_dict:
            old_key = self.get_least_frequent(self.item_dict)
            print("DISCARD:", old_key)
            self.cache_data.pop(old_key)
            self.item_dict.pop(old_key)
        self.item_dict[key] = self.item_dict.get(key, 0) + 1
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a value from the cache by key.

        Args:
            key: The key whose value needs to be retrieved.

        Returns:
            The value associated with the key if it exists, None otherwise.
        """
        if key and key in self.item_dict:
            self.item_dict[key] += 1
        return self.cache_data.get(key, None)
