# """reading data from telnet connection"""
# import socket

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# server_address = ("127.0.0.1", 8010)
# server_socket.bind(server_address)
# server_socket.listen()

# try:
#     connection, client_address = server_socket.accept()
#     print(f"Got connection request from {client_address}")
    
#     buffer = b""
#     while buffer[-2:] != b"\r\n":
#         data = connection.recv(2)
#         if not data:
#             break
#         else:
#             print(f"Got data: {data}")
#             buffer = buffer + data
#     print(f"whole the data {buffer}")
#     connection.sendall(buffer)
# finally:
#     server_socket.close()

# import socket

# SIZE = 2

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# server_address = ("127.0.0.1", 8010)
# server_socket.bind(server_address)
# server_socket.listen()

# connections = []

# try:
#     connection, client_address = server_socket.accept()
#     connections.append(connection)
#     # вынеснеие connections из while True для получения последующих сообщений
#     while True:
#         # connection, client_address = server_socket.accept()
#         # print(f"got connection request from {client_address}")
#         # connections.append(connection)

#         for connection in connections:
#             buffer = b""
#             while buffer[-2:] != b"\r\n":
#                 data = connection.recv(SIZE)
#                 if not data:
#                     break
#                 else:
#                     print(f"Got data {data}")
#                     buffer = buffer + data
#             # encoding = chardet.detect(buffer)["encoding"]
#             connection.sendall(buffer)
#             print(f"Whole the data: {buffer}")  # .decode('utf-8')}")

# finally:
#     server_socket.close()

# import socket

# SIZE = 2

# srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

# srv_address = ("127.0.0.1", 8010)
# srv_socket.bind(srv_address)
# srv_socket.setblocking(False)
# srv_socket.listen()

# connections = list()

# try:
#     while True:
#         try:
#             connection, cl_address = srv_socket.accept()
#             connection.setblocking(False)
#             connections.append(connection)
#             print(f"Got connection request from {cl_address}") 
#         except Exception as e:
#             print(str(e))
#             pass

#         for connection in connections:
#             try:
#                 buffer = b""
#                 while buffer[-2:] != b"\r\n":
#                     data = connection.recv(SIZE)
#                     if not data:
#                         break
#                     else:
#                         buffer = buffer + data
#                         print("got", data)
#                 connection.sendall(buffer)
#                 # connection.send(buffer)
#                 print(f"Whole the data are {buffer.decode('ascii')}")
#             except Exception as e:
#                 print(str(e), "ha")
#                 pass
# finally:
#     srv_socket.close()
