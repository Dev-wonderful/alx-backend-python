#!/usr/bin/env python3
'''Double co-routines application'''
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """run wait random n times"""
    delay_list: List[float] = []
    for _ in range(n):
        delay: float = await wait_random(max_delay)
        delay_list.append(delay)
    return sorted(delay_list, key = lambda x:float(x))
