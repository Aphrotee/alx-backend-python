#!/usr/bin/env python3

'''
This module provides the function `measure_time`
'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    This function measures the total execution time for
    wait_n(n, max_delay), and returns total_time / n.
    '''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
