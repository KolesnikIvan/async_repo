import asyncio

def make_request():
    future = asyncio.Future()
    asyncio.create_task(set_future(future))
    return future

async def set_future(future:asyncio.Future):
    await asyncio.sleep(1)
    future.set_result(42)

async def main():
    future = make_request()
    print(f"is request done? {future.done()}")
    value = await future
    print(f"is request done? {future.done()}")
    print(value)

asyncio.run(main())
