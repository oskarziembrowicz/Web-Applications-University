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

# MAX_LENGTH = 20
# def fitTheMessage(message):
#     if len(message) < MAX_LENGTH:
#         while len(message) < MAX_LENGTH:
#             message += ' '
#     elif len(message) > MAX_LENGTH:
#         message = message[slice(0, MAX_LENGTH)]
#     return message
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2901))
#     client_socket.send(fitTheMessage('Hello').encode())
#     data = client_socket.recv(1024)
#     if data:
#         print(f"Recieved: {data.decode()}")
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#======================================================================

# Zad9

datagram = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"

src_port_hex = datagram[0:4]
dst_port_hex = datagram[4:8]
data_hex = datagram[16:]

src_port = int(src_port_hex, 16)
dst_port = int(dst_port_hex, 16)
data_length = int((len(data_hex)*4)/8)
data = bytes.fromhex(data_hex).decode('ascii')

output = f"zad14odp;src;{src_port};dst;{dst_port};data;{data}"

print(output)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)

try:
    client_socket.connect(('127.0.0.1', 2901))
    client_socket.send(output.encode())
    data = client_socket.recv(1024)
    if data:
        print(f"Recieved: {data.decode()}")
    else:
        print("No data recieved :(")
except socket.error as e:
    print(f"Socket error: {e}")

client_socket.close()