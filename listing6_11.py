"""shared value with two processes"""
from multiprocessing import Process, Value

def increment_value(shared_value: Value):
    shared_value.value += 1

if __name__ == "__main__":
    for _ in range(100):
        shared_value = Value ('i', 0)
        procs = [
            Process(target=increment_value, args=(shared_value,)),
            Process(target=increment_value, args=(shared_value,))
        ]

        [p.start() for p in procs]
        [p.join() for p in procs]

        print(shared_value.value)
        assert shared_value.value == 2
        