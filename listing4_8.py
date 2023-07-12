"""asyncio,as_completed() method example"""
import asyncio
import random

import aiohttp


async def fetch_status(session:aiohttp.ClientSession, 
                       url:str, 
                       pause: int = 0):
    await asyncio.sleep(pause)
    async with session.get(url) as result:
        # time.sleep(pause)
        print("pause", pause)
        return result.status
    

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["http:\\example.com" for _ in range(7)]
        tasks = [fetch_status(session, url, random.randint(1,7)) for url in urls]
        for finished_task in asyncio.as_completed(tasks):
            print('the result is')
            print(await finished_task)

asyncio.run(main())
