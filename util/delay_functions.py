import asyncio

async def delay(delay_seconds:int)-> int:
    print(f"start sleep for {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"end sleep {delay_seconds} seconds")
    return delay_seconds
