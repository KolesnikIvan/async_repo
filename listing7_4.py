"""1one thoisand requests example with asyncio"""
import asyncio
from concurrent.futures import ThreadPoolExecutor
import functools
import requests
import time

from util.async_deco import async_timed

def get_status(url: str)->int:
    response = requests.get(url)
    return response.status_code

@async_timed()
async def main():
    loop: asyncio.AbstarctEventLoop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=100) as pool:
        urls = ["https://www.example.com" for _ in range(100)]
        tasks = [
            loop.run_in_executor(
                pool,\
                functools.partial(get_status, url))\
                for url in urls
        ]
        results = await asyncio.gather(*tasks)
        print(results)
asyncio.run(main())
