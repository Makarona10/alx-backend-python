#!/usr/bin/env python3

'''Basic annotations for variables'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    '''returns a function that multiplies a float by multiplier'''
    def returnFunc(second: float) -> float:
        return second * multiplier
    return returnFunc
