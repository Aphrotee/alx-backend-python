#!/usr/bin/env python3

"""
This module provides the function `sum_mixed_list`
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    This is a type-annotated function that takes
    a list mxd_lst of integers
    """
    result: float = 0.00
    for value in mxd_lst:
        result += value
    return result
