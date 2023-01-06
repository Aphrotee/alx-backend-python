#!/usr/bin/env python3

"""
This module provides the function `safeky_get_value`
"""

import typing

T = typing.TypeVar('T')
def safely_get_value(dct: typing.Mapping[typing.Any, typing.Any], key: typing.Any, default: typing.Union[typing.Any, None] = None) -> typing.Union[T, typing.Any, None]:
    """
    This function returns the value of the key in the dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default