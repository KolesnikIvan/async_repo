"""echo server with threading and error handling"""
# from collections.abc import Callable, Iterable, Mapping
# import socket
# from threading import Thread
# from typing import Any

# class ThreadWithErrorHandling(Thread):
#     def __init__(self, client):
#         super().__init__()
#         self.client = client
    
#     def run(self):
#         try:
#             while True:
#                 data = self.client.recv(2048)
#                 if not data:
#                     raise BrokenPipeError("cconnection is closed")
#                 print(f"got data {data}")
#                 self.client.sendall(data)
#         except OSError as e:
#             print(f"got exception {e}; now stopping")
#             self.client.close()
#         finally:
#             print("closed")

#     def close(self):
#         print("disconnected")
#         if self.is_alive():
#             self.client.sendall(bytes("STOPPING"), encoding="utf-8")
#             self.client.shutdown(socket.SHUT_RDWR)


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
#     server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     srv_addr = ("127.0.0.1", 8010)
#     server.bind(srv_addr)
#     server.listen()
#     connected_threads = list()
#     try:
#         while True:
#             connection, addr = server.accept()
#             thread = ThreadWithErrorHandling(connection)
#             thread.start()
#             connected_threads.append(thread)
#     except Exception as e:
#         print(f"stop server because of {e}")
#         for tr in connected_threads:
#             tr.close()
#             print(f"closed {thread}")

#         # server.shutdown()
#     finally:
#         print("bye bye")    

from collections.abc import Callable, Iterable, Mapping
import socket
from threading import Thread
from typing import Any

class ThreadWithErrorHandling(Thread):
    def __init__(self, client):
        super().__init__()
        self.client = client
    
    def run(self):
        try:
            while True:
                data = self.client.recv(2048)
                if not data:
                    raise BrokenPipeError("Appplication is closed")
                print("got data {data}")
                self.client.sendall(data)
        except OSError as e:
            print(f"got exception {str(e)}")

    def close(self):
        print("closing client socket")
        socket.close(socket.SHUT_RDWR)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_Addr = ("127.0.0.1", 8010)
    server.bind(srv_Addr)
    server.listen()
    connected_threads = list()
    try:
        while True:
            connection, addr = server.accept()
            print(f"got connection request from {addr}")
            thread = ThreadWithErrorHandling(connection)
            thread.start()
            connected_threads.append(thread)
    except BrokenPipeError:
        server.shutdown()
        for thr in connected_threads:
            print("Stopping")
            thr.close()
