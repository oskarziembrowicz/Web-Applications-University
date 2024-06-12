import socket
import ssl

HOST = '127.0.0.1'
PORT = 2905

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket = ssl.wrap_socket(server_socket, server_side=True, keyfile='lb11ex5server.key', certfile='lb11ex5server.crt')

server_socket.bind((HOST, PORT))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()

    try:
        data = client_socket.recv(4096)
        if data:
            print(f"Recieved a message: {data.decode()}")
            client_socket.send(data)
    except:
        client_socket.close()
