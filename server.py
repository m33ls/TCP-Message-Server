import socket
import sys

address = "localhost"
port = 81

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (address, port)
tcp_socket.bind(server_address)

tcp_socket.listen(1)

while True:
    print("Awaiting connection...")
    connection, client = tcp_socket.accept()

    try:
        print(f"Client connection: {client}")

        while True:
            data = connection.recv(32)
            print(f"Received data: {data}")

            if not data:
                break
    finally:
        connection.close()
