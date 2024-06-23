#!/usr/bin/env python3
'''async comprehension'''
import asyncio
from 0_async_generator import async_generator


async def async_comprehension():
    '''generates a list of 10 random numbers'''
    return [i async for i in async_generator()]
