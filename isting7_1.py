"""simple example of multithread echo server 
from previous part
using threading package
"""
import socket
from threading import Thread

def echo(client: socket):
    while True:
        data = client.recv(2048)
        client.sendall(data)
        print(f"got data {data}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_addr = ("127.0.0.1", 8010)
    server.bind(srv_addr)
    server.listen()
    while True:
        connection, addr = server.accept()
        print(f"got connection from {addr}")
        thread = Thread(target=echo, args=(connection,))
        thread.start()
