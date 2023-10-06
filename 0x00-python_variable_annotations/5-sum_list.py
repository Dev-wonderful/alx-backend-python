#!/usr/bin/env python3
"""addition of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """add and return float"""
    sum: float = 0.0
    for input in input_list:
        sum += input
    return sum
