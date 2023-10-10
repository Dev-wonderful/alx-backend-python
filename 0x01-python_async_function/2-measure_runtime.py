#!/usr/bin/env python3
"""runtime measurement module"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time taken per execution of wait_random"""
    loop = asyncio.get_event_loop()
    start_time = time.time()
    loop.run_until_complete(wait_n(n, max_delay))
    end_time = time.time()
    loop.close()
    runtime = end_time - start_time
    average_runtime = runtime / n
    return average_runtime
