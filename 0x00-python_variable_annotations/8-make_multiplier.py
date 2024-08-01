#!/usr/bin/env python3

'''Basic annotations for variables'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by multiplier'''
    return lambda x: multiplier * x
