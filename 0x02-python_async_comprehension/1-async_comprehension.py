#!/usr/bin/env python3
'''async comprehension'''
import asyncio
async_generator = __import__('0_async_generator').async_generator


async def async_comprehension():
    '''generates a list of 10 random numbers'''
    return [i async for i in async_generator()]
