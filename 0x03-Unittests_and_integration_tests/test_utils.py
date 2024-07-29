#!/usr/bin/env python3
""" This module contains unit tests for a access_nested_map function """
import unittest
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
        This class is a unittest for access_nested_map function.
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), (1)),
            ({"a": {"b": 2}}, ("a",), ({"b": 2})),
            ({"a": {"b": 2}}, ("a", "b"), (2))
            ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map with different nested maps and paths.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path of keys to access in the nested map.
            expected: The expected value from the nested map.

        Asserts:
            The value obtained from access_nested_map is equal to the
            expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
