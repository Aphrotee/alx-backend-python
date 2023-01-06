#!/usr/bin/env python3

"""
This module provides the function `safe_first_element`
"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any])\
                        -> typing.Union[typing.Any, None]:
    """
    This function returns the first element of
    the input if it exists otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
