# import socket
# import selectors
# from selectors import SelectorKey
# from typing import List, Tuple

# SIZE = 2
# selector = selectors.DefaultSelector()

# srv_socket = socket.socket()  # socket.AF_INET, socket.SOCKET_STREAM)
# srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# srv_addr = ("127.0.0.1", 8010)
# srv_socket.setblocking(False)
# srv_socket.bind(srv_addr)
# srv_socket.listen()

# selector.register(srv_socket, selectors.EVENT_READ)
# connections = list()

# while True:
#     events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)
#     if len(events) == 0:
#         print("No events. Wait more.")
    
#     for event, _ in events:
#         event_socket = event.fileobj

#         if event_socket == srv_socket:
#             connection, cl_addr = srv_socket.accept()
#             print(f"got connection request from {cl_addr}")
#             connection.setblocking(False)
#             selector.register(connection, selectors.EVENT_READ)
#         else:
#             data = connection.recv(SIZE)
#             print(f"got data {data}")
#             event_socket.send(data)


# import socket
# import selectors
# from selectors import DefaultSelector, SelectorKey
# from typing import List, Tuple

# SIZE = 2

# selector = DefaultSelector()

# srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# srv_addr = ("127.0.0.1", 8010)
# srv_socket.bind(srv_addr)
# srv_socket.setblocking(False)
# srv_socket.listen()

# selector.register(srv_socket, selectors.EVENT_READ)

# while True:
#     events: List[Tuple(SelectorKey, int)] = selector.select(timeout=1)

#     if len(events) == 0:
#         print("no connections; wait more")

#     for event in events:
#         event_socket = event.fileobj()

#         if event_socket == srv_socket:
#             connection, addr = event_socket.accept()
#             connection.setblocking(False)
#             print(f"got connection request from {addr}")
#         else:
#             data = event_socket.recv()
#             event_socket.send(data)
#             print(f"got {data}")

import socket
import selectors
from selectors import DefaultSelector, SelectorKey
from typing import List, Tuple
SIZE = 1024

selector = DefaultSelector()

srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

srv_addr = ("127.0.0.1", 8010)
srv_socket.bind(srv_addr)
srv_socket.listen()
srv_socket.setblocking(False)

selector.register(srv_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)

    if len(events) == 0:
        print("there are no connections; continue waiting")

    for event, _ in events:
        event_socket = event.fileobj

        if event_socket == srv_socket:
            connection, cl_addr = event_socket.accept()
            connection.setblocking(False)
            print(f"got connection from {cl_addr}")
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(SIZE)
            event_socket.sendall(data)
            print(f"got {data}")
