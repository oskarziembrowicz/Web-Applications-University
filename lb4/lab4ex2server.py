import socket
import datetime
HOST = '127.0.0.1'
PORT = 2900

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

print("Waiting for clients...")

connected_clients_sockets.append(server_socket)


while True:
    client_socket, client_address = server_socket.accept()
    print("Client connected")
    try:
        data = client_socket.recv(4096)
        if data:
            print(f"Recieved a message: {data.decode()}")
            client_socket.send(data)
    except:
        client_socket.close()

server_socket.close()