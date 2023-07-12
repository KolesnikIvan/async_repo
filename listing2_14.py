"""future objects introduction"""
from asyncio import Future

my_future = Future()
print(f" my_future is done {my_future.done()}")
my_future.set_result(41)
print(f"myfuture is done {my_future.done()}")
print(f"my_future result {my_future.result()}")
