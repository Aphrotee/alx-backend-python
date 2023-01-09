#!/usr/bin/env python3

"""
This module provides the asyunc function `wait_random`
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ This function waits for a random delay between
    0 and max_delay seconds and eventually returns it. """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
