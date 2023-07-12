"""asyncio.run() in debug mode"""
import asyncio
from util import async_timed

@async_timed()
async def cpu_bound_task() -> int:
    counter = 0
    for i in range(100000000):
        counter += 1
    return counter

@async_timed()
async def main() -> None:
    task1 = asyncio.create_task(cpu_bound_task())
    await task1

asyncio.run(main(), debug=True)
