"""reenterable lock example recursion"""
from threading import Thread
from threading import Lock, RLock

# list_lock = Lock()
list_lock = RLock()

def sum_list(int_list: list[int])-> int:
    print("Waiting for lock")
    with list_lock:
        print("got lock")
        if len(int_list) == 0:
            print("sum complete")
            return 0
        else:
            head, *tail = int_list
            print(head)
            return head + sum_list(tail)
thread = Thread(target=sum_list, args=([1,2,3,4],))
thread.start()
thread.join()
