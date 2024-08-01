#!/usr/bin/env python3

'''Basic annotations for variables'''

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    return (tuple((k, float(v * v))))
