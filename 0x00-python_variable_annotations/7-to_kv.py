#!/usr/bin/env python3
"""convert to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert to tuple"""
    return k, v ** 2
