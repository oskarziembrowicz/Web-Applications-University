import shutil
import socket

# ==============================================

# Zad1
# print("Enter a .txt file path to copy")
# f1 = input()
#
# shutil.copyfile(f1, "lab1zad1.txt")

# ======================================================

# Zad2
# print("Enter a .png file path to copy")
# f2 = input()
#
# shutil.copyfile(f2, "lab1zad1.png")

# =======================================================

# Zad3
# import socket
#
# print("Enter ip address")
# ip_address = input()
#
# try:
#     socket.inet_aton(ip_address)
#     print("ip address is correct")
# except socket.error:
#     print("ip address is incorrect")

# ========================================================

# Zad4
# print("Enter ip address")
# ip_address = input()
#
# try:
#     hostname = socket.gethostbyaddr(ip_address)[0]
#     print(f"Hostname is: {hostname}")
# except socket.herror:
#     print("Couldn't find hostname")

# ===================================================================

# Zad5
# print("Enter hostname")
# hostname = input()
# ip_address = socket.gethostbyname(hostname)
# print(f"Ip address is: {ip_address}")

# ========================================================================

# Zad6
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
#         client_socket.connect((host, port))
#         print("Connected")
#
#         client_socket.close()
#     except socket.error as e:
#         print(f"Error: {e}")
#
# except socket.error:
#     print("ip address is incorrect")

# =============================================================

# Zad7
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
#         client_socket.settimeout(0.5)
#
#         result = client_socket.connect_ex((host, port))
#
#         if result == 0:
#             print(f"Port {port} is open")
#
#         client_socket.close()
#     except socket.error as e:
#         pass

# =========================================================================
