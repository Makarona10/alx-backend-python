#!/usr/bin/env python3

'''0x02. Python - Async Comprehension'''

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> 'list[float]':
    '''return the 10 random numbers'''
    return [i async for i in async_generator()]

