import socket, select
from random import randint
HOST = '127.0.0.1'
PORT = 2914

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

print("Waiting for clients...")

connected_clients_sockets.append(server_socket)

random_number = randint(1, 100)
print(f"Generated number: {random_number}")

while True:
    read_socket, write_socket, error_socket = select.select(connected_clients_sockets, [], [])

    for client in read_socket:

        if client == server_socket:
            client_socket, client_address = server_socket.accept()
            connected_clients_sockets.append(client_socket)
            print("Client connected")
        else:
            try:
                data = client.recv(1024)
                if data:
                    print(f"Recieved a message: {data.decode()}")
                    try:
                        number = int(data.decode())
                        message = ''
                        if number == random_number:
                            message = "Congratulations! You guessed it!"
                            random_number = randint(1, 100)
                            print("Number was guessed")
                            print(f"New generated number: {random_number}")
                        elif number < random_number:
                            message = "Wrong! Too low"
                        elif number > random_number:
                            message = "Wrong! Too high"
                        print(f"Sending message: {message}")
                        client.send(message.encode())
                    except Exception as e:
                        message = "Incorrect type " + e
                        client.send(message.encode())
            except:
                client.close()
                connected_clients_sockets.remove(client)
                print("Client disconnected")
                continue

server_socket.close()