#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests"""

from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)
        
    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map: Mapping, key: Sequence) -> None:
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, key)



if __name__ == '__main__':
    unittest.main()