#!/usr/bin/env python3
"""make multiplication"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make multiplier"""
    def fun(*args: float):
        """inside function"""
        for arg in args:
            sum = arg * multiplier
        return sum
    return fun
