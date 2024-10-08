#!/usr/bin/env python3

'''Async await python'''

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n'''
    s = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.time() - s
    return 0 if n == 0 else elapsed / n
