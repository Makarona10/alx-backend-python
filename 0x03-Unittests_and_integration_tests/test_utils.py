#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests"""

from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([({"a": 1}, ["a"], 1),
                           ({"a": {"b": 1}}, ["a"], {"b": 1}),
                           ({"a": {"b": 2}}, ["a", "b"], 2)
                           ])
    def test_access_nested_map(self, nested_map, path, expected):
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)
