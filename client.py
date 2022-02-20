import socket

address = "localhost"
port = 81

tcp_socket = socket.create_connection((address, port))

data = bytes(input("Type a message: "), 'utf-8')
tcp_socket.sendall(data)

data_from_server = str(tcp_socket.recv(1024))
print(f"Message from server: {data_from_server}")
