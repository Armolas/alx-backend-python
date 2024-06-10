#!/usr/bin/env python3
'''basic async syntax'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for
    a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds. Default is 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)  # Wait for the delay
    return delay  # Return the delay time
