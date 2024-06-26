#!/usr/bin/python3
""" 0-basic_cache Module """

BaseCaching = __import__("base_caching").BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache class is a simple caching system that inherits from BaseCaching.
    It allows storing and retrieving key-value pairs in a dictionary.

    Methods:
        __init__(self, *args, **kwargs): Initializes the BasicCache instance.
        put(self, key, item): Adds a key-value pair to the cache.
        get(self, key): Retrieves a value from the cache by key.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BasicCache instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        super().__init__(*args, **kwargs)

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
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