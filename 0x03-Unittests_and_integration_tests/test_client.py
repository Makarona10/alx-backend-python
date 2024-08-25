#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests"""

from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from typing import Mapping, Sequence
import requests
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    
    @parameterized.expand([
        ('google'),
        ('abc')])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        test_class = GithubOrgClient(org_name)
        test_class.org()
        print(mock)
        mock.called_with_once(test_class.ORG_URL.format(org=input))

    def test_public_repos_url(self):
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "Hello World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('get_json')
    def test_public_repos(self, mock_get_json):
        mock_get_json.return_value = {'payload': True}
        with patch('GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = 'chosen payload'
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
            expected = {'payload': True}
            self.assertEqual(result, expected)
            mock.assert_called_once()
            mock_get_json.assert_called_once()
