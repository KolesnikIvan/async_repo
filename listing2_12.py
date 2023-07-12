"""setting timeout using asyncio.wait_for"""
import asyncio
from util import delay

async def main():
    delay_task = asyncio.create_task(delay(5))

    try:
        result = await asyncio.wait_for(delay_task, timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print("Time-out")
        print(f"task is done {delay_task.done()}; task is cancelled {delay_task.cancelled()}")

asyncio.run(main())
