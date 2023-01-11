#!/usr/bin/env python3

'''
This is a module that provides the coroutine async_comprehension
'''

import random
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    This is a coroutine that collects 10 random numbers
    using an async comprehensing over async_generator,
    then return the 10 random numbers
    '''
    return [num async for num in async_generator()]
