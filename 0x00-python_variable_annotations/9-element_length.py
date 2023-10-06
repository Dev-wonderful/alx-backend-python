#!/usr/bin/env python3
"""Annotate function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence]]:
    """Annotate the function"""
    return [(i, len(i)) for i in lst]