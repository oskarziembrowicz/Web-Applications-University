import socket

# Zad13

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
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2910))
#     client_socket.send(output.encode())
#     response = client_socket.recv(1024)
#     print(response.decode())
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# ===============================================================

# Zad14

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
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2909))
#     client_socket.send(output.encode())
#     response = client_socket.recv(1024)
#     print(response.decode())
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# =======================================================================

# Zad15