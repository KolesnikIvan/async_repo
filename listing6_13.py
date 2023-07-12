"""shared objects in the process pool"""
# # from concurrent.futures import ProcessPoolExecutor
# # from multiprocessing import Value
# # import asyncio

# # shared_counter: Value

# # def init(counter: Value):
# #     global shared_counter
# #     shared_counter = counter

# # def increment():
# #     with shared_counter.get_lock():
# #         shared_counter.value += 1

# # async def main():
# #     counter = Value('d', 0)
# #     with ProcessPoolExecutor(initializer=init,
# #                              initargs=(counter,)) as proc_pool:
# #         await asyncio.get_runnig_loop().run_in_executor(proc_pool, increment)


# # if __name__ == "__main__":
# #     asyncio.run(main())


# from concurrent.futures import ProcessPoolExecutor
# import asyncio
# from multiprocessing import Value


# shared_counter: Value

# def init(counter: Value):
#     global shared_counter
#     shared_counter = counter

# def increment():
#     with shared_counter.get_lock():
#         shared_counter.value += 1

# async def main():
#     counter = Value('d', 0)
#     with ProcessPoolExecutor(initializer=init, 
#                              initargs=(counter,)) as pool:
#         await asyncio.get_running_loop().run_in_executor(pool, increment)
#         print(counter.value)
    
# if __name__ == "__main__":
#     asyncio.run(main())

from concurrent.futures import ProcessPoolExecutor
import asyncio
from multiprocessing import Value

shared_counter: Value

def init(counter: Value):
    global shared_counter
    shared_counter = counter

def increment():
    with shared_counter.get_lock():
        shared_counter.value += 1

async def main():
    counter = Value("d", 0)
    with ProcessPoolExecutor(initializer=init,
                             initargs=(counter,)) as pool:
        await asyncio.get_running_loop().run_in_exectutor(pool, increment)

if __name__ == "__main__":
    asyncio.run(main())
