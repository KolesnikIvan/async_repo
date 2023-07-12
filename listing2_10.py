import asyncio
from util import delay

async def hello_per_sec():
    for i in range(2):
        await asyncio.sleep(1)
        print(f"hello while other code works; {i}")

async def main():
    wait1 = asyncio.create_task(delay(3))
    wait2 = asyncio.create_task(delay(3))
    await hello_per_sec()
    await wait1
    await wait2
    print("the end")

asyncio.run(main())