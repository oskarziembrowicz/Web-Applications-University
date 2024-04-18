import socket

# Zad1

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)

try:
    client_socket.connect(('127.0.0.1', 2912))
    data = ''.encode()
    while(data.decode() != "You won! This is the right number!"):
        number = input("Enter your number: ")
        client_socket.send(number.encode())
        data = client_socket.recv(1024)
        if data:
            print(data.decode())
        else:
            print("No data recieved :(")
except socket.error as e:
    print(f"Socket error: {e}")

client_socket.close()