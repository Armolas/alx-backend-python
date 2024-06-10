#!/usr/bin/env python3
'''measure time'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average time per coroutine.
    """
    start_time = time.perf_counter()  # Start the timer
    await wait_n(n, max_delay)  # Execute the coroutine
    end_time = time.perf_counter()  # End the timer
    total_time = end_time - start_time  # Calculate the total elapsed time
    return total_time / n  # Return the average time per coroutine
