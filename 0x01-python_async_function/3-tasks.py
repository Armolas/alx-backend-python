#!/usr/bin/env python3
'''task wait random'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
