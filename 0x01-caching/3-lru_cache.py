#!/usr/bin/env python3
""" 3-lru_cache """
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class is a caching system that follows
        the Least Recently Used (LRU) principle.

    Attributes:
        item_list (list): A list to keep track of the order of item usage.

    Methods:
        __init__(self): Initializes the LRUCache instance.
        put(self, key, item): Adds a key-value pair to the cache,
            removing the least recently used item if necessary.
        get(self, key): Retrieves a value from the cache by key.
    """
    def __init__(self):
        """
        Initializes the LRUCache instance.
        """
        super().__init__()
        self.item_list = []

    def put(self, key, item):
        """
        Adds a key-value pair to the cache. If the cache is full, removes
        the least recently used item.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return

        # set last used items
        if key in self.item_list:
            self.item_list.pop(self.item_list.index(key))
        elif len(self.cache_data) == BaseCaching.MAX_ITEMS\
                and key not in self.item_list:
            leased_used_item = self.item_list.pop(0)
            print("DISCARD:", leased_used_item)
            self.cache_data.pop(leased_used_item)

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
