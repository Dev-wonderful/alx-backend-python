#!/usr/bin/env python3
"""async comprehension for python"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Creating a List using async comprehension"""
    return [i async for i in async_generator()]