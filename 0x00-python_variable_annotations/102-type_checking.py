#!/usr/bin/env python3

"""
This module provides the function `zoom_array`
"""

import typing


def zoom_array(lst: typing.Tuple, factor: int = 2) -> typing.List:
    """
    This function returns a zoomed in list
    """
    zoomed_in: typing.List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
