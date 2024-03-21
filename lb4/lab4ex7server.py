import socket
import datetime
HOST = '127.0.0.1'
PORT = 2901
MAX_MESSAGE_LENGTH = 20

def recv_message(client_socket):
    message = ''
    recievedBytes = 0

    while recievedBytes < MAX_MESSAGE_LENGTH:
        segment = client_socket.recv(MAX_MESSAGE_LENGTH - recievedBytes).decode()

        if not segment:
            break

        message += segment
        recievedBytes += len(segment)

    return message

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
        message = recv_message(client_socket)
        print(f"Recieved a message: {message}")
        client_socket.send(message.encode())
    except:
        client_socket.close()

server_socket.close()