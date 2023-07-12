import aiohttp

async def fetch_status(session: aiohttp.ClientSession,
                       url: str):
    async with session.get(url) as result:
        return result.status