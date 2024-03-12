import socket

# Zad1

# import struct
# import time
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(5)
# TIME_1970 = 2208988800
#
# try:
#     client_socket.connect((socket.gethostbyname('ntp.task.gda.pl'), 123))
#     client_socket.send(b'\x1b' + 47 * b'\0')
#     data = client_socket.recv(1024)
#     if data:
#         t = struct.unpack('!12I', data)[10]
#         t -= TIME_1970
#     print(time.ctime(t))
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# ========================================================

# Zad2

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

# =================================================

# Zad3

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2900))
#     while (True):
#         message = input()
#         client_socket.send(message.encode())
#         print(client_socket.recv(1024))
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# ===================================================

# Zad4

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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

# =====================================================

# Zad5

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2901))
#     while (True):
#         message = input()
#         client_socket.send(message.encode())
#         print(client_socket.recv(1024))
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# =============================================

# Zad6

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2901))
#     num1 = input("Enter a number: ")
#     op = input("Enter an operator: ")
#     num2 = input("Enter another number: ")
#     client_socket.send(num1.encode())
#     client_socket.send(op.encode())
#     client_socket.send(num2.encode())
#     print(client_socket.recv(1024))
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# =======================================

# Zad7

# host = input("Enter ip address or hostname: ")
# port = int(input("Enter port number: "))
# if not(host[0].isnumeric()):
#     host = socket.gethostbyname(host)
#
# try:
#     socket.inet_aton(host)
#     print("ip address is correct")
#     try:
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client_socket.settimeout(5)
#         client_socket.connect((host, port))
#         service = socket.getservbyport(port)
#         print(f"Service on port {port}: {service}")
#         print("Connected")
#         client_socket.close()
#     except socket.error as e:
#         print(f"Error: {e}")
#         print("This port may not be open")
#
# except socket.error:
#     print("ip address is incorrect")

# ==============================================

# Zad8

# host = input("Enter ip address or hostname: ")
# if not(host[0].isnumeric()):
#     host = socket.gethostbyname(host)
#
# print("Ports range")
# port_start = int(input("Enter starting port: "))
# port_end = int(input("Enter ending port: "))
#
# for port in range(port_start, port_end):
#     try:
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client_socket.settimeout(0.3)
#
#         if client_socket.connect_ex((host, port)) == 0:
#             service = socket.getservbyport(port)
#             print(f"Port {port} is open - service: {service}")
#
#         client_socket.close()
#     except socket.error as e:
#         pass

# ===========================================================

# Zad9

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(10)
#
# try:
#     client_socket.connect(('127.0.0.1', 2906))
#     print("Connected!")
#     client_socket.send('0.0.0.0'.encode())
#     print(f'Hostname: {client_socket.recv(1024).decode()}')
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# =============================================================

# Zad10

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(10)
#
# try:
#     client_socket.connect(('127.0.0.1', 2907))
#     print("Connected!")
#     client_socket.send('example.org'.encode())
#     print(f'Host ip: {client_socket.recv(1024).decode()}')
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# ================================================================

# Zad11

# MAX_LENGTH = 20
#
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
#     client_socket.connect(('127.0.0.1', 2908))
#     print("Connected!")
#     message = input("Enter the message of maximum length of 20: ")
#     message = fitTheMessage(message)
#     print(f"Message: {message}, Message length: {len(message)}")
#
#     client_socket.send(message.encode())
#     print(f'Message: {client_socket.recv(MAX_LENGTH).decode()}')
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

# =========================================================================

# Zad12

# MAX_LENGTH = 20
#
# def splitIntoMessages(message, singleMessageLength):
#     messages = [message[i:i + singleMessageLength] for i in range(0, len(message), singleMessageLength)]
#     if len(messages[-1]) < singleMessageLength:
#         while len(messages[-1]) < singleMessageLength:
#             messages[-1] += ' '
#     return messages
#
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2908))
#     print("Connected!")
#     message = input("Enter the message: ")
#
#     if len(message) > MAX_LENGTH:
#         message_chunks = splitIntoMessages(message, MAX_LENGTH)
#
#     # print(message_chunks)
#     for msg in message_chunks:
#         client_socket.send(msg.encode())
#         print(f'Message: {client_socket.recv(MAX_LENGTH).decode()}')
#
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()