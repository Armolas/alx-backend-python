#!/usr/bin/env python3
'''measure runtime'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''measures the runtime of async comprehension'''
    start_time = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end_time = time.perf_counter()
    return end_time - start_time
