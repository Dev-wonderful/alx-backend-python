#!/usr/bin/env python3
"""measure runtime for async comprehension"""
from typing import List
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List:
    """measure runtime for async comprehension in parallel"""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()
    result = end_time - start_time
    return result
