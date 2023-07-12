import asyncio
from util import delay

async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0

    while not long_task.done():
        print(f"long_task is on; {seconds_elapsed}")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed >= 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.CancelledError:
        print(f"task {long_task} was taken off")

asyncio.run(main())
