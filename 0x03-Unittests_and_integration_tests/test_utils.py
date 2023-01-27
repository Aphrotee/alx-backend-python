#!/usr/bin/env python3

"""
This module supplies the test case `TestAccessNestedMap`
"""

import parameterized
import unittest
from unittest.mock import patch
import utils
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """ A Class for testing the function `access_nested_map` """

    @parameterized.parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({"a": {"b": 2}}, ('a',), {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ Test for `access_nested_map` """
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test for `access_nested_map` exeption """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ A class for testing the function `get_json` """

    @parameterized.parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_payload(self, url, payload, mock_get):
        """ Test for `get_json` """
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = payload
        self.assertEqual(utils.get_json(url), payload)
        mock_get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ A class for testing the function decorator `memoize` """

    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch('test_utils.TestMemoize.TestClass.a_method')
    def test_memoize(self, mock_method):
        """ Test for `memoize` """
        mock_method.return_value = self.TestClass.a_method
        testClass = self.TestClass()
        self.assertEqual(testClass.a_property, testClass.a_property)
        mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
