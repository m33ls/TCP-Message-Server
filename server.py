import socket

address = "localhost"
port = 81

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (address, port)
tcp_socket.bind(server_address)

tcp_socket.listen(10)
print("Awaiting connection...")

connection, client = tcp_socket.accept()
print(f"Client connection: {client}")

data = connection.recv(1024)
print(f"Received data: {data}")
    
connection.sendall(data)
connection.close()
