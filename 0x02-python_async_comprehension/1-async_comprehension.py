#!/usr/bin/env python3

'''0x02. Python - Async Comprehension'''

from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    async for i in async_generator():
        yield i
