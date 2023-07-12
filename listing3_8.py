# import socket
# import asyncio
# from asyncio import AbstractEventLoop

# async def echo(connection: socket, loop:AbstractEventLoop):
#     while data := await loop.sock_recv(connection, 1024):
#         await loop.sock_sendall(connection, data)


# async def listen_for_connection(server_socket:socket,
#                                 loop: AbstractEventLoop):
#     while True:
#         connection, addr = loop.socket_accept(server_socket)
#         connection.setblocking(False)
#         print(f"got connection request from {addr}")
#         asyncio.create_task(echo(connection, loop))

# async def main():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 1)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#     srv_addr = ("127.0.0.1", 8010)
#     server_socket.bind(srv_addr)
#     server_socket.setblocking(False)
#     server_socket.listen()

#     await listen_for_connection(server_socket, asyncio.get_event_loop())

#     asyncio.run(main())

# import asyncio
# from asyncio import AbstractEventLoop
# import socket

# async def echo(connection: socket, loop: AbstractEventLoop):
#     while data := await loop.sock_recv(connection, 1024):
#         print(f"got data {data}")
#         await loop.sock_sendall(connection, data)

# async def listen_for_connection(srv_socket: socket, loop: AbstractEventLoop):
#     while True:
#         connection, addr = loop.sock_accept(srv_socket)
#         connection.setblocking(False)
#         print(f"got connection request from {addr}")
#         asyncio.create_task(echo(connection, loop))

# async def main():
#     srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#     srv_addr = ("127.0.0.1", 8010)
#     srv_socket.bind(srv_addr)
#     srv_socket.setblocking(False)
#     srv_socket.listen()

#     await listen_for_connection(srv_socket, asyncio.get_event_loop())
#     asyncio.run(main())

# import asyncio
# import socket
# from asyncio import AbstractEventLoop

# tasks = []
# async def echo(connection: socket,
#  loop: AbstractEventLoop) -> None:
#     try:
#         while data := await loop.sock_recv(connection, 1024):
#             if data == b"boom":
#                 raise Exception("Net error")
#             print(f"got {data}")
#             await loop.sock_sendall(connection, data)
#     except Exception as e:
#         print("EXCEPPTIONN", str(e))
#     finally:
#         connection.close()

# async def listen_for_connection(server_socket: socket,
#  loop: AbstractEventLoop):
#     while True:
#         connection, address = await loop.sock_accept(server_socket)
#         connection.setblocking(False)
#         print(f"Получен запрос на подключение от {address}")
#         # tasks.append(asyncio.create_task(echo(connection, loop)))
#         asyncio.create_task(echo(connection, loop))
        
# async def main():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_address = ('127.0.0.1', 8010)
#     server_socket.setblocking(False)
#     server_socket.bind(server_address)
#     server_socket.listen()
#     await listen_for_connection(server_socket, asyncio.get_event_loop())
    
# asyncio.run(main())

import asyncio
from asyncio import AbstractEventLoop
import socket

async def echo(connection: socket, loop: AbstractEventLoop):
    try:
        while data := await loop.sock_recv(connection, 1024):
            await loop.sock_sendall(connection, data)
    finally:
        connection.close()    

async def listen_for_connections(srv_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, addr = await loop.sock_accept(srv_socket)
        connection.setblocking(False)
        asyncio.create_task(echo(connection, loop))

async def main():
    srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv_addr = ("127.0.0.1", 8010)
    srv_socket.bind(srv_addr)
    srv_socket.setblocking(False)
    srv_socket.listen()

    await listen_for_connections(srv_socket, asyncio.get_event_loop())

asyncio.run(main())
