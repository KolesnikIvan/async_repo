# import threading
# import os

# print(f"process {os.getpid()} is on")

# def hello_threading():
#     print(f"from fun process {os.getpid} is on")
#     print(f"from fun {threading.current_thread()} is on")

# hello_thr = threading.Thread(target=hello_threading)
# hello_thr.start()

# total_threads = threading.active_count()
# thread_name = threading.current_thread().name

# print(f"thread name is {thread_name}")
# print(f"total {total_threads} is (are) on")
# hello_thr.join()
# print('end')

import multiprocessing
import os

def hello_from_process():
    print(f"hello from process {os.getpid()}")

if __name__ == "__main__":
    hello_proc = multiprocessing.Process(target=hello_from_process)
    hello_proc.start()

    print(f"Hello from parent process {os.getpid()}, {os.getppid()}.")

    hello_proc.join()
