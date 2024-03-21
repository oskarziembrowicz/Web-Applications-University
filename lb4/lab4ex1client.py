import socket

# Zad 1,2

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)

try:
    client_socket.connect(('127.0.0.1', 2900))
    client_socket.send('Hello'.encode())
    data = client_socket.recv(4096)
    if data:
        print(f"Recieved: {data.decode()}")
    else:
        print("No data recieved :(")
except socket.error as e:
    print(f"Socket error: {e}")

client_socket.close()