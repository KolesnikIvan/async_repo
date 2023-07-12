"""shared resource woth threads exmple: requests progress supervision monitoring"""
import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import functools

import requests

counter: int = 0
counter_lock = Lock()

def get_status(url: str) -> int:
    global counter
    response = requests.get(url)
    with counter_lock:
        counter += 1
    return response.status_code

async def reporter(request_count: int):
    while counter < request_count:
        print(f"done {counter}/{request_count} requests")
        await asyncio.sleep(.2)

async def main():
    request_count = 200
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        urls = ["https://www.example.com" for _ in range(request_count)]
        supervisor_task = asyncio.create_task(reporter(request_count))
        tasks = [loop.run_in_executor(\
            pool,\
            functools.partial(get_status, url)) for url in urls
        ]
        results = await asyncio.gather(*tasks)
        await supervisor_task
        print(results)

asyncio.run(main())
