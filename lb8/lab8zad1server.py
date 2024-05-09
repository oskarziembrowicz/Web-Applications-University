import socket, threading

HOST = '127.0.0.1'
PORT = '2900'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

print("Server is listening")

def serve(client, client_address):
    try:
        data = client.recv(4096)
        if data:
            client.send(data)
            print(f'Sending data to: {client_address}')

    except:
        print(f'Disconnected from client {client_address}')
        client.close()

while True:

        client, client_address = server_socket.accept()
        threading.Thread(target=serve, args=(client, client_address)).start()
server_socket.close()