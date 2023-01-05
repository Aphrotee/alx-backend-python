#!/usr/bin/env python3

"""
This module provides the function `element_length`
"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence]) ->\
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    This function takes a list lst as argument
    """
    return [(i, len(i)) for i in lst]
