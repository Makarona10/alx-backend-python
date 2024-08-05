#!/usr/bin/env python3

'''Async await python'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    an asynchronous coroutine that takes in an integer argument and
    waits for a random delay between 0 and max_delay and eventually returns it
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
