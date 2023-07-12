"""racing state?"""
from threading import Lock, Thread
import time

lock_a = Lock()
lock_b = Lock()

def a():
    with lock_a:
        print("got a lock from method a()")
        time.sleep(1)
        with lock_b:
            print("got both lock from method a()")

def b():
    with lock_b:
        print("got lock_b from method b()")
        time.sleep(1)
        with lock_a:
            print("got both lock from method b()")

thread_a = Thread(target=a)
thread_b = Thread(target=b)
thread_a.start()
thread_b.start()
thread_a.join()
thread_b.join()
