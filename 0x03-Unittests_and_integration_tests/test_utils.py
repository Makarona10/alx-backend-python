#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests"""

from utils import access_nested_map, get_json
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping, Sequence
import requests


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """unit test for utils.access_nested_map"""
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)
        
    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence) -> None:
        """test that a KeyError is raised for the specific inputs"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get_json):
        mock_get_json.return_value.json.return_value = test_payload
        res = get_json(test_url)
        self.assertEqual(res, test_payload)
        mock_get_json.assert_called_once_with(test_url)
