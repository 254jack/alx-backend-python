#!/usr/bin/env python3
""" async coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Args:
            max_delay: max async

        Return:
            random float time
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
