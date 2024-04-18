#!/usr/bin/env python3
"""Firaol Tulu Task 8: Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This Function Creates a multiplier function."""
    return lambda x: x * multiplier
