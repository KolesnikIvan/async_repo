import asyncio
from util import delay

async def main():
    a_task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(a_task), timeout=5)
        print("hello result", result)
    except asyncio.TimeoutError:
        print("task takes more than 5 s, soon it will be done")
        result = await a_task
        print(result)

asyncio.run(main())
