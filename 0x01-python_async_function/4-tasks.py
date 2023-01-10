#!/usr/bin/env python3

"""
This module provides the function `task_wait_n`
"""

import typing
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    This function that takes in 2 int arguments n and max_delay,
    runs the task task_wait_random with the specified max_delay and
    returns the list of all the delays in ascending order.
    """
    delays: typing.List[float] = []
    delay: float = 0.0
    for i in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
    delaysT = tuple(delays)
    delays = list(sorted(delaysT))
    return delays
