#!/usr/bin/env python3

'''
This module provides the coroutine  async_generator
'''

import typing
import asyncio
import random


async def async_generator() -> typing.Generator[float, None, None]:
    '''
    This is a coroutine that loops 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
