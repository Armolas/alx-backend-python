#!/usr/bin/env python3
'''This module contains make_multilier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a multilier function'''
    def multiply(n: float) -> float:
        '''retuns n multilied by multiplier'''
        return n * multiplier
    return multiply
