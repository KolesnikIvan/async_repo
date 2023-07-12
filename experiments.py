# Введение в библиотеку multiprocessing 159
# import time
# from multiprocessing import Process

# def count(count_to: int) -> int:
#     start = time.time()
#     counter = 0
#     while counter < count_to:
#         counter = counter + 1
#     end = time.time()
#     print(f'Закончен подсчет до {count_to} за время {end-start}')
#     return counter

# if __name__ == "__main__":
#     start_time = time.time()
#     to_one_hundred_million = Process(target=count, args=(100000000,))
#     to_two_hundred_million = Process(target=count, args=(200000000,))
#     to_one_hundred_million.start()
#     to_two_hundred_million.start()
#     to_one_hundred_million.join()
#     to_two_hundred_million.join()
#     end_time = time.time()
#     print(f'Полное время работы {end_time-start_time}')
    

# from concurrent.futures import ProcessPoolExecutor

# if __name__ == "__main__":
#     with ProcessPoolExecutor() as process_pool:
#         numbers = [1, 1000, 3, 500, 5, 22, 1e08]
#         # for i, result in enumerate(process_pool.map(count, numbers)):
#         #     print(i, result)
#         for res in process_pool.map(count, numbers):
#             print(res)

import time
from concurrent.futures import ProcessPoolExecutor

def count(count_to: int) -> int:
    start = time.time()
    counter = 0 
    while counter < count_to:
        counter += 1
    print("got result in ", (time.time() - start))
    return counter

if __name__ == "__main__":
    with ProcessPoolExecutor() as process_pool:
        numbers = [1, 3, 5, 22, 1e06]
        for res in process_pool.map(count, numbers):
            print(res)


def partition(data: List,
              chunk_size: int):
    for i in range(len(data), chunk_size):
        yield data[i, i + chunk_size]





def partition(data: list, chunk_size:int):
    for i in range(len(data), chunk_size):
        yield data[i, i+chunk_size]
        