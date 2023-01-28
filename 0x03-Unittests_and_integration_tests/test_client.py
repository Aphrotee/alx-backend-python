#!/usr/bin/env python3

"""
This module provides test cases `TestGithubOrgClient`
"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
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
from parameterized import (
    parameterized,
    parameterized_class
)


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


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(TestCase):
    """A class for GithubOrgClient Integration test"""

    @classmethod
    def setUpClass(cls):
        """
        Mocks requests.get to return example
        payloads found in the fixtures
        """
        def sideEffect(url):
            """ Side Effect """
            url = url.split('/')
            if url[len(url) - 1] == 'repos':
                return Mock(**{'json.return_value': cls.repos_payload})
            return Mock(**{'json.return_value': cls.org_payload})

        cls.get_patcher = patch('utils.requests.get', side_effect=sideEffect)
        cls.get_patcher.start()

    def test_public_repos(self):
        """ Test for `public_repos` """
        git = GithubOrgClient('google')
        self.assertListEqual(git.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test for `public_repos` with license """
        git = GithubOrgClient('google')
        license = "apache-2.0"
        self.assertListEqual(git.public_repos(license), self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """ Stop patcher """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
