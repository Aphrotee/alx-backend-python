#!/usr/bin/env python3

""" This module provides the function `to_kv` """

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ This function takes a string k and an int OR float v as arguments and
        returns a tuple. The first element of the tuple is the string k. The
        second element is the square of the int/float v and should be annotated
        as a float. """
    return (k, v ** 2)
