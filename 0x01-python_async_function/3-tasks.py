#!/usr/bin/env python3
"""create async task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an async task"""
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(wait_random(max_delay))
    # loop.close()
    task = asyncio.create_task(wait_random(max_delay))
    return task
