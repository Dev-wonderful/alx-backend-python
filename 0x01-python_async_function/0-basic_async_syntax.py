#!/usr/bin/env python3
"""Wait random function"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """randomizes the wait period"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
