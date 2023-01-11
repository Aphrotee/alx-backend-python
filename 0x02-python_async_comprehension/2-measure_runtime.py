#!/usr/bin/env python3

'''
This is module provides the coroutine measure_runtime
'''

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    This is a coroutine that executes async_comprehension
    four times in parallel using asyncio.gather and
    measures the total runtime and return it.
    '''
    start: float = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return time.perf_counter() - start
