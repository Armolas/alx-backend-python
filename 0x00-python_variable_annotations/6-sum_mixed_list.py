#!/usr/bin/env python3
'''mixed list sum module'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''returns the sum of a list of floats and ints'''
    total: float = 0.0
    for value in mxd_list:
        total += value
    return total
