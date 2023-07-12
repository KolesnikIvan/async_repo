import asyncio
from util import delay

async def main():
    print("start")
    sleep_for_3 = asyncio.create_task(delay(3))
    print("type of sleep for 3", type(sleep_for_3))
    result = await sleep_for_3
    print(f"{result}")

asyncio.run(main())
