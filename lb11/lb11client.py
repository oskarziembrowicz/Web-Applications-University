import socket, ssl
import requests

# Zad2

# A)

# url = "http://httpbin.org/html"
# headers = {'user-agent': 'Safari/7.0.3'}
# response = requests.get(url, headers=headers, verify=False)
# print(f"Response status: {response.status_code}")
# file = open("lab5ex1response.html", "w")
# file.write(response.text)
# file.close()
#
# file = open("lab11ex2response.html", "r")
# print(file.read())
# file.close()

# B)

# url = "http://httpbin.org/html"
# headers = {'user-agent': 'Safari/7.0.3'}
# response = requests.get(url, headers=headers, cert='server.crt')
# print(f"Response status: {response.status_code}")
# file = open("lab5ex1response.html", "w")
# file.write(response.text)
# file.close()
#
# file = open("lab5ex1response.html", "r")
# print(file.read())
# file.close()

#=========================================

# Zad3

# chat.freenode.net
#============================================

# Zad5

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)
client_socket = ssl.wrap_socket(client_socket, server_side=False, keyfile='lb11ex5server.key', certfile='lb11ex5server.crt')

try:
    client_socket.connect(('127.0.0.1', 2905))
    client_socket.send('Hello'.encode())
    data = client_socket.recv(4096)
    if data:
        print(f"Recieved: {data.decode()}")
    else:
        print("No data recieved :(")
except socket.error as e:
    print(f"Socket error: {e}")

client_socket.close()

#============================================

# Zad6


