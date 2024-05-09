import socket

# Zad 1

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)

try:
    client_socket.connect(('127.0.0.1', 2900))
    client_socket.send(b'Hello')
    print(client_socket.recv(1024))
except socket.error as e:
    print(f"Socket error: {e}")

client_socket.close()