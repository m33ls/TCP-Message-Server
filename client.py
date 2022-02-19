import socket
import sys

address = "localhost"
port = 81

tcp_socket = socket.create_connection((address, port))

try:
    data = bytes(input("Type a message: "), 'utf-8')
    tcp_socket.sendall(data)

finally:
    print("Closing socket...")
    tcp_socket.close()
