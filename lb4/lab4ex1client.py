import socket

# Zad 1,2,3

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2900))
#     client_socket.send('Hello'.encode())
#     data = client_socket.recv(4096)
#     if data:
#         print(f"Recieved: {data.decode()}")
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# ============================================

# Zad4

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2900))
#     client_socket.send('2+6'.encode())
#     data = client_socket.recv(1024)
#     if data:
#         print(f"Recieved: {data.decode()}")
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#=============================================================

# Zad5

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2900))
#     client_socket.send('0.0.0.0'.encode())
#     data = client_socket.recv(1024)
#     if data:
#         print(f"Recieved: {data.decode()}")
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#============================================================

# Zad6

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2901))
#     client_socket.send('example.com'.encode())
#     data = client_socket.recv(1024)
#     if data:
#         print(f"Recieved: {data.decode()}")
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#=====================================================

# Zad7

MAX_LENGTH = 20
def fitTheMessage(message):
    if len(message) < MAX_LENGTH:
        while len(message) < MAX_LENGTH:
            message += ' '
    elif len(message) > MAX_LENGTH:
        message = message[slice(0, MAX_LENGTH)]
    return message

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)

try:
    client_socket.connect(('127.0.0.1', 2901))
    client_socket.send(fitTheMessage('Hello').encode())
    data = client_socket.recv(1024)
    if data:
        print(f"Recieved: {data.decode()}")
    else:
        print("No data recieved :(")
except socket.error as e:
    print(f"Socket error: {e}")

client_socket.close()