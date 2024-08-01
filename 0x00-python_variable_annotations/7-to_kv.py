#!/usr/bin/env python3

'''Basic annotations for variables'''

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    '''Returns a tuple contains the first arg and the second's
    square as a float'''
    return (tuple((k, float(v * v))))
