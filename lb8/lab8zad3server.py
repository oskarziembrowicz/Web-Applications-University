import socket, threading
from random import randint
HOST = '127.0.0.1'
PORT = 2902

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

lock = threading.Lock()

print("Waiting for clients...")

def serve(client):
    random_number = randint(1, 100)
    print(f"Generated number: {random_number}")
    end_connection = False
    try:
        while(True):
            data = client.recv(1024)
            if data:
                print(f"Recieved a message: {data.decode()}")
                try:
                    number = int(data.decode())
                    message = ''
                    if number == random_number:
                        message = "Congratulations! You guessed it!"
                        end_connection = True
                        print("Number was guessed")
                    elif number < random_number:
                        message = "Wrong! Too low"
                    elif number > random_number:
                        message = "Wrong! Too high"
                    print(f"Sending message: {message}")
                    client.send(message.encode())
                    if end_connection:
                        break;
                except Exception as e:
                    message = "Incorrect type " + e
                    client.send(message.encode())
    finally:
        client.close()
        print("Client disconnected")

while True:

    client, client_address = server_socket.accept()
    print(f'Connected to client: {client_address}')
    threading.Thread(target=serve, args=(client,)).start()
server_socket.close()