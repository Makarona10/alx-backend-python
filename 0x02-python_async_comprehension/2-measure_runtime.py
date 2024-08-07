#!/usr/bin/env python3

'''0x02. Python - Async Comprehension'''

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''execute async_comprehension four times
    in parallel using asyncio.gather'''
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return time.perf_counter() - s
