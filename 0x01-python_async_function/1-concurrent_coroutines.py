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
    length = len(delay_list)
    for i in range(length):
        swapped = False
        for j in range(0, n-i-1):
            if delay_list[j] > delay_list[j+1]:
                delay_list[j], delay_list[j+1] = delay_list[j+1], delay_list[j]
                swapped = True
        if not swapped:
            break

    return delay_list
