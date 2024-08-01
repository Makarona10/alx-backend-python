#!/usr/bin/env python3

'''Basic annotations for variables'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple contains the first arg and the second's
    square as a float'''
    return (tuple((k, v**2)))
