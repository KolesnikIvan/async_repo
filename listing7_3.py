"""threadpool executor"""
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time
import requests

REQUESTS_NUMBER = 100

def get_status(url: str)->int:
    response = requests.get(url)
    return response.status_code

def synchronous_variant():
    for _ in range(REQUESTS_NUMBER):
        res = get_status("https://www.example.com")
        print(res)

start = time.time()

with ThreadPoolExecutor(max_workers=1000) as pool:
    urls = ["https://www.example.com" for _ in range(REQUESTS_NUMBER)]
    results = pool.map(get_status, urls)
    for result in results:
        print(result)
    
    end = time.time()
    print(f"poll.map had done in {end - start:.4f} seconds")

    # tasks = [asyncio.create_task(get_status, url) for url in urls]
    # results = asyncio.gathe(*tasks)
    # end2 = time.time()
    # print(f"asyncio.gather() had done in {end2-end:.4f} seconds")

    start = time.time()
    synchronous_variant()
    end = time.time()
    print(f"synchronous version had done it in {end - start:.4f} seconds")
