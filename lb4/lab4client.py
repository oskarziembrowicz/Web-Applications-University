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

# datagram = "ed740b550024effd70726f6772616d6d696e6720696e20707974686f6e2069732066756e"
#
# src_port_hex = datagram[0:4]
# dst_port_hex = datagram[4:8]
# data_hex = datagram[16:]
#
# src_port = int(src_port_hex, 16)
# dst_port = int(dst_port_hex, 16)
# data_length = int((len(data_hex)*4)/8)
# data = bytes.fromhex(data_hex).decode('ascii')
#
# output = f"zad14odp;src;{src_port};dst;{dst_port};data;{data}"
#
# print(output)
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2901))
#     client_socket.send(output.encode())
#     data = client_socket.recv(1024)
#     if data:
#         print(f"Recieved: {data.decode()}")
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#==========================================================

# Zad10

# datagram = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
# datagram = datagram.replace(' ', '')
#
# src_port_hex = datagram[0:4]
# dst_port_hex = datagram[4:8]
# # data_hex = datagram[int(192/4):]
# data_hex = datagram[int(256/4):]
#
# print(data_hex)
#
# src_port = int(src_port_hex, 16)
# dst_port = int(dst_port_hex, 16)
# data = bytes.fromhex(data_hex).decode('utf-8')
#
# output = f"zad13odp;src;{src_port};dst;{dst_port};data;{data}"
#
# print(output)
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2901))
#     client_socket.send(output.encode())
#     data = client_socket.recv(1024)
#     if data:
#         print(f"Recieved: {data.decode()}")
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#============================================

# Zad11

datagram = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"
datagram = datagram.replace(' ', '')

protocol_ver_hex = datagram[0]

SRC_IP_START = int(96/4)
SRC_IP_END = int(128/4)
src_ip_hex = datagram[SRC_IP_START:SRC_IP_END]

DST_IP_START = int(128/4)
DST_IP_END = int(160/4)
dst_ip_hex = datagram[DST_IP_START:DST_IP_END]

PROTOCOL_START = int(72/4)
PROTOCOL_END = int(80/4)
protocol_hex = datagram[PROTOCOL_START:PROTOCOL_END]

protocol_ver = int(protocol_ver_hex, 16)

src_ip = int(src_ip_hex, 16)
dst_ip = int(dst_ip_hex, 16)
src_ip = socket.inet_ntoa(src_ip.to_bytes(4, byteorder='big'))
dst_ip = socket.inet_ntoa(dst_ip.to_bytes(4, byteorder='big'))

protocol = int(protocol_hex, 16)

outputA = f'zad15odpA;ver;{protocol_ver};srcip;{src_ip};dstip;{dst_ip};type;{protocol}'

# Ports:

if protocol == 6:
    # TCP
    print("TCP protocol")
    SRC_PORT_START = int(160 / 4)
    SRC_PORT_END = int(176 / 4)
    DST_PORT_START = int(176 / 4)
    DST_PORT_END = int(192 / 4)
    DATA_START = int(416 / 4)
elif protocol == 17:
    # UDP
    print("UDP protocol")
    SRC_PORT_START = int(160 / 4)
    SRC_PORT_END = int(176 / 4)
    DST_PORT_START = int(176 / 4)
    DST_PORT_END = int(192 / 4)
    DATA_START = int(224 / 4)
else:
    # Wrong
    print("Error: Incorrect protocol!")

src_port_hex = datagram[SRC_PORT_START:SRC_PORT_END]
dst_port_hex = datagram[DST_PORT_START:DST_PORT_END]
data_hex = datagram[DATA_START:]

src_port = int(src_port_hex, 16)
dst_port = int(dst_port_hex, 16)
data = bytes.fromhex(data_hex).decode('ascii')

outputB = f'zad15odpB;srcport;{src_port};dstport;{dst_port};data;{data}'

# CONNECTING TO SERVER

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)

try:
    client_socket.connect(('127.0.0.1', 2901))

    print(outputA)
    client_socket.send(outputA.encode())
    responseA = client_socket.recv(1024)
    print(responseA.decode())
    if responseA.decode() == 'TAK':
        print(outputB)
        client_socket.send(outputB.encode())
        responseB = client_socket.recv(1024)
        print(responseB.decode())
    else:
        print("Incorrect data!")
except socket.error as e:
    print(f"Socket error: {e}")

client_socket.close()