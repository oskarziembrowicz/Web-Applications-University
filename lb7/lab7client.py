import socket
import time
from itertools import permutations

# Zad1

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2912))
#     data = ''.encode()
#     while(data.decode() != "You won! This is the right number!"):
#         number = input("Enter your number: ")
#         client_socket.send(number.encode())
#         data = client_socket.recv(1024)
#         if data:
#             print(data.decode())
#         else:
#             print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#========================================================

# Zad2

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     client_socket.connect(('127.0.0.1', 2914))
#     data = ''.encode()
#     while(data.decode() != "Congratulations! You guessed it!"):
#         number = input("Enter your number: ")
#         client_socket.send(number.encode())
#         data = client_socket.recv(1024)
#         if data:
#             print(data.decode())
#         else:
#             print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()

#=============================================================

# Zad3

# Searching for UDP sequence
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(10)
#
# udp_sequence = []
#
# udp_port = 11666
# while udp_port <= 65535:
#     try:
#         client_socket.connect(('127.0.0.1', udp_port))
#         # data = ''.encode()
#         client_socket.send("PING".encode())
#         data = client_socket.recv(1024)
#         if data:
#             print(data.decode())
#             if data.decode() == "PONG":
#                 udp_sequence.append(udp_port)
#         else:
#             print("No data recieved :(")
#     except socket.error as e:
#         print(f"Socket error: {e}")
#     udp_port += 1000
#
# print(udp_sequence)
#
# print("Trying to unlock TCP port with UDP sequence permutations")
#
# udp_perm = permutations(udp_sequence)
# client_socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket_tcp.settimeout(10)
#
# for perm in udp_perm:
#     for udp in perm:
#         client_socket.connect(('127.0.0.1', udp))
#         client_socket.send("PING".encode())
#         data = client_socket.recv(1024)
#         # print(data.decode())
#
#     # Connecting to TCP
#     try:
#         client_socket_tcp.connect(('127.0.0.1', 2913))
#         client_socket_tcp.send("Hello".encode())
#         data = client_socket_tcp.recv(1024)
#         if data:
#             print(data.decode())
#             if(data.decode() == "Congratulations! You found the hidden"):
#                 break
#     except socket.error as e:
#         print(f"Socket error: {e}")
#
# client_socket.close()
# client_socket_tcp.close()

#==================================================================

# Zad4
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.settimeout(5)
#
# try:
#     udp_time_start = time.time_ns()
#     client_socket.connect(('127.0.0.1', 2915))
#     # udp_time_start = time.time_ns()
#     client_socket.send('Hello'.encode())
#     data = client_socket.recv(1024)
#     if data:
#         print(f"Recieved: {data.decode()}")
#         udp_time_end = time.time_ns()
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.settimeout(5)
#
# try:
#     tcp_time_start = time.time_ns()
#     client_socket.connect(('127.0.0.1', 2916))
#     # tcp_time_start = time.time_ns()
#     client_socket.send('Hello'.encode())
#     data = client_socket.recv(1024)
#     if data:
#         print(f"Recieved: {data.decode()}")
#         tcp_time_end = time.time_ns()
#     else:
#         print("No data recieved :(")
# except socket.error as e:
#     print(f"Socket error: {e}")
#
# client_socket.close()
#
# print(f"UDP time (ns): {udp_time_end - udp_time_start}")
# print(f"TCP time (ns): {tcp_time_end - tcp_time_start}")

# Komunikacja zazwyczaj w obu przypadkach jest natychmiastowa, ale jeśli pojawiają się opóźnienia, to częściej w przypadku TCP i mają większe prawdopodobieństwo być bardziej znaczące niż w UDP
# Wynika to z tego, że TCP poświęca dodatkowy czas na potwierdzenie pakietów
# UDP jest szybsze ale zapewnia mniejszą gwarancję poprawności pakietów
# TCP jest wolniejsze ale dokładniejsze