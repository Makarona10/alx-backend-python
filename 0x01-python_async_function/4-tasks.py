#!/usr/bin/env python3

'''Async await python'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    async routine called that takes in 2 int arguments and
    return the list of all the delays
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    compl = []
    for res in asyncio.as_completed(tasks):
        compl.append(await res)
    return compl
