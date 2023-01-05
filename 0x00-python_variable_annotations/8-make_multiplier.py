#!/usr/bin/env python3

"""
This module provides the function `make_multiplier`
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    This function takes a float multiplier as argument
    """
    def multiplier(flt: float) -> float:
        """
        This function takes a float flt as argument
        """
        return flt * multiplier
    return multiplier
