#!/usr/bin/env python3

"""
This module supplies the test cases `TestAccessNestedMap`,
`TestGetJson` and `TestMemoize`
"""

from parameterized import parameterized
from typing import (
    Tuple,
    Union,
    Dict,
    Callable
)
import unittest
from unittest.mock import patch, Mock

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """ A Class for testing the function `access_nested_map` """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({"a": {"b": 2}}, ('a',), {"b": 2}),
        ({"a": {"b": 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               result: Union[Dict, int]) -> None:
        """ Test for `access_nested_map` """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str]) -> None:
        """ Test for `access_nested_map` exeption """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ A class for testing the function `get_json` """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_payload(self,
                     test_url: str,
                     test_payload: Dict) -> None:
        """ Test for `get_json` """
        attrs = {'json.return_value': test_payload}
        with patch('utils.requests.get',
                   return_value=Mock(**attrs)) as mock_get:
            # mock_get.return_value.ok = True
            # mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ A class for testing the function decorator `memoize` """

    class TestClass:

        def a_method(self) -> int:
            return 42

        @memoize
        def a_property(self) -> int:
            return self.a_method()

    @patch('test_utils.TestMemoize.TestClass.a_method')
    def test_memoize(self,
                     mock_method: Callable) -> None:
        """ Test for `memoize` """
        mock_method.return_value = self.TestClass.a_method
        testClass = self.TestClass()
        self.assertEqual(testClass.a_property, testClass.a_property)
        mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
