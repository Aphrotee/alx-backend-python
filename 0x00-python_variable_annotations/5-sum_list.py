#!/usr/bin/env python3

"""
This module provides the function `sum_list`.
"""


def sum_list(input_list: list[float]) -> float:
    """
    This function takes a list input_list of floats
    as argument and returns their sum as a float.
    """
    result: float = 0.00
    for value in input_list:
        result += value
    return result
    