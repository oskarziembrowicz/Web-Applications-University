import socket, ssl
import requests

# Zad2


url = "http://httpbin.org/html"

# A)

# headers = {'user-agent': 'Safari/7.0.3'}
# response = requests.get(url, headers=headers, verify=False)
# print(f"Response status: {response.status_code}")
# file = open("lab5ex1response.html", "w")
# file.write(response.text)
# file.close()
#
# file = open("lab5ex1response.html", "r")
# print(file.read())
# file.close()

# B)

headers = {'user-agent': 'Safari/7.0.3'}
response = requests.get(url, headers=headers, cert='server.crt')
print(f"Response status: {response.status_code}")
file = open("lab5ex1response.html", "w")
file.write(response.text)
file.close()

file = open("lab5ex1response.html", "r")
print(file.read())
file.close()

#=========================================

# Zad3

# chat.freenode.net
#============================================

# Zad5

#============================================

# Zad6


