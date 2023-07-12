# import asyncio

# import aiohttp

# from util.chapter4 import fetch_status


# async def main():
#     async with aiohttp.ClientSession() as session:
#         urls = ["https://example.com" for _ in range(1000)]
#         requests = [await fetch_status(session, url) for url in urls]
#         # results = await asyncio.gather(*requests)
#         # print(results)
#         print(requests)
#         # input()

# asyncio.run(main())

import asyncio
import aiohttp

async def fetch_status(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as result:
        return result.status

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://example.com" for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*requests)
        print(results)

asyncio.run(main())
