#!/usr/bin/env python3
"""Firaol Tulu Task 9: Let's duck type an iterable object
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This Fuction Computes the length of a list of sequences."""
    return [(i, len(i)) for i in lst]
