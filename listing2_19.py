"""combine account and long dauer tasks"""
"""example not to mix account and input/output tasks"""
import asyncio
from util import async_timed, delay

@async_timed()
async def cpu_bound_task() -> int:
    counter = 0
    for i in range(10000000):
        counter += 1
    return counter

@async_timed()
async def main():
    task1 = asyncio.create_task(cpu_bound_task())
    task2 = asyncio.create_task(cpu_bound_task())
    task3 = asyncio.create_task(delay(4))
    await task1
    await task2
    await task3

asyncio.run(main())
