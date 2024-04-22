#!/usr/bin/env python3

"""Task 1: Let's execute multiple coroutines"""

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function return the list of all the delays (float values)"""
    waits = await asyncio.gather(*list(map(lambda _: wait_random(max_delay), range(n))))

    return sorted(waits)
