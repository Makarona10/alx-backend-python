#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests"""

from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, Mock
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
        mock.called_with_once(test_class.ORG_URL.format(org=input))
