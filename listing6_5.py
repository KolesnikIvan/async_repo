"""asynchronous loop, process pool and executors"""
import asyncio
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import time

def count(count_to: int) -> int:
    start = time.time()
    counter = 0 
    while counter < count_to:
        counter += 1
    print("got result in ", (time.time() - start))
    return counter

async def main():
    with ProcessPoolExecutor() as process_pool:
        loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
        numbers = [1, 3, 5, 22, 1e06]
        calls = [partial(count, number) for number in numbers]
        coro = []

        for call in calls:
            coro.append(loop.run_in_executor(process_pool, call))

        res = await asyncio.gather(*coro)
        print(*res)

if __name__ == "__main__":
    asyncio.run(main())
