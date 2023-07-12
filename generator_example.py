# import time
# from itertools import islice

# def timed(f):
#     def wrap(*args, **kwargs):
#         time1 = time.time()
#         ret = f(*args, **kwargs)
#         print("took", time.time() - time1)
#         return ret
#     return wrap

# @timed
# def use_genr():
#     return list(islice((time.sleep(x) for x in range(3)), 1))

# @timed
# def use_list():
#     return list(islice([time.sleep(x) for x in range(3)], 1))

# print(use_genr())
# print(use_list())

# print(type((time.sleep(x) for x in range(3))))
# print(type([time.sleep(x) for x in range(3)]))

# from itertools import islice


# def positive_integer(until: int):
#     for integer in range(until):
#         yield integer

# positive = positive_integer(7)

# print(next(positive))
# print(*islice(positive, 2))
# print(next(positive))
# print(*islice(positive, 3))


# import asyncio

# from util.delay_functions import delay

# async def async_gen(until: int):
#     for integer in range(until):
#         # asyncio.sleep(delay(integer))
#         await delay(integer)
#         yield integer
        
# async def main():
#     async_generator = async_gen(5)
#     print(type(async_generator))
#     async for i in async_generator:
#         print("got ", i)

# asyncio.run(main())

# import asyncio
# from util.delay_functions import delay

# async def async_gen(until: int):
#     for integer in range(until):
#         asyncio.sleep(delay(integer))
#         yield(integer)


# async def main():
#     as_gen = async_gen(3)
#     async for item in as_gen:
#         print(item)

# asyncio.run(main())

import asyncio

from util.delay_functions import delay

async def async_gen(until: int):
    for integer in range(until):
        await delay(integer)
        yield integer
    
async def main():
    asnnc_gen = async_gen(5)
    async for i in asnnc_gen:
        print(i)


asyncio.run(main())
