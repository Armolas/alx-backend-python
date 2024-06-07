#!/usr/bin/env python3
'''this module contains the to_kv functon'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple of string and float'''
    return (k, v * v)
