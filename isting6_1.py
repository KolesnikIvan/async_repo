"""about shared memory"""
from multiprocessing import Process, Value, Array

def increment_value(shared_int: Value):
    shared_int.value += 1

def increment_array(shared_array: Array):
    for index, integer in enumerate(shared_array):
        shared_array[index] = integer + 1

if __name__ == "__main__":
    shared_value = Value('i', 0)
    shared_array = Array('i', [0, 0])

    procs = [
        Process(target=increment_value, args=(shared_value,)),
        Process(target=increment_array, args=(shared_array,))
    ]

    [p.start() for p in procs]
    [p.join() for p in procs]

    print('val____', shared_value.value)
    print('arr____', shared_array[:])
