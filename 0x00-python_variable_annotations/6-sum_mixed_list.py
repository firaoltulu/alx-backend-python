#!/usr/bin/env python3
"""Firaol Tulu Task 6: Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This Function Computes the sum of a list of integers and floating-point numbers."""
    return float(sum(mxd_lst))
