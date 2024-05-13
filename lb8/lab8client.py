import socket

# Zad 1

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2900))
#     client_socket.send(b'Hello')
#     print(client_socket.recv(1024))
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#==================================================

# Zad 2

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2901))
#     client_socket.send(b'Hello')
#     print(client_socket.recv(1024))
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#===================================================

# Zad 3

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)

try:
    client_socket.connect(('127.0.0.1', 2902))
    data = ''.encode()
    while(data.decode() != "Congratulations! You guessed it!"):
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