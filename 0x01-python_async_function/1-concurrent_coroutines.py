#!/usr/bin/env python3

"""
This module provides the function `wait_random`
"""

import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    This function that takes in 2 int arguments n and max_delay,
    spawns wait_random n times with the specified max_delay and
    returns the list of all the delays in ascending order.
    """
    delays: typing.List[float] = []
    delay: float = 0.0
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    delaysT = tuple(delays)
    delays = list(sorted(delaysT))
    return delays
