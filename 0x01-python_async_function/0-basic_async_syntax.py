#!/usr/bin/env python3
"""Task 0: The basics of async Write an asynchronous."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This Function waits for a random number of seconds"""
    wait_seconds: float = random.random() * max_delay
    await asyncio.sleep(wait_seconds)
    return wait_seconds
