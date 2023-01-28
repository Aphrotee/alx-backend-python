#!/usr/bin/env python3

"""
This module provides test cases `TestGithubOrgClient`
"""

from client import GithubOrgClient
from typing import (
    Callable
)
import unittest
from unittest import TestCase
from unittest.mock import (
    patch,
    PropertyMock,
    Mock
)
from utils import get_json
from parameterized import parameterized


class TestGithubOrgClient(TestCase):
    """ A class for testing `GithubOrgClient` """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json', autospec=True)
    def test_org(self,
                 name: str,
                 mock_get_json: Callable) -> None:
        """ Test for `org` """
        git = GithubOrgClient(name)
        mock_get_json.return_value = {}
        git.org
        mock_get_json.assert_called_once_with(git.ORG_URL.format(org=name))

    @patch('test_client.GithubOrgClient.org',
           new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """ Test for `public_repos_url` """
        payload = {
            'paylooad': True,
            'repos_url': 'https://github.com/aprotee'
        }
        with patch('test_client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = Mock()
            mock_org.return_value = payload
            git = GithubOrgClient('aprotee')
            self.assertEqual(git._public_repos_url,
                             payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Tests for `public repos` """
        payload = [
            {'name': 'alx-backend'},
            {'name': 'zero_day'},
            {'name': 'alx-backend_python'}
        ]
        mock_get_json.return_value = payload
        with patch('test_client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            mock_pru.return_value = 'https://github.com/aprotee'
            git = GithubOrgClient('Aphrotee')
            self.assertListEqual(git.public_repos(),
                                 [
                                    'alx-backend',
                                    'zero_day',
                                    'alx-backend_python'
                            ])
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, response):
        """ Test for `has_license` """
        git = GithubOrgClient('aphrotee')
        self.assertEqual(git.has_license(repo, license_key), response)


if __name__ == '__main__':
    unittest.main()
