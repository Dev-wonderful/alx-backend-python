#!/usr/bin/env python3
"""addition of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """add and return float"""
    sum: float = 0.0
    for input in mxd_list:
        sum += input
    return sum
