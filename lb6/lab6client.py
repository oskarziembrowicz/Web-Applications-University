import socket

# Zad 6

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(5)

print(socket.gethostbyname("interia.pl"))

try:
    client_socket.connect((socket.gethostbyname("interia.pl"), 587))
    client_socket.send("EHLO testowanieaplikacji.edu.pl".encode())
    response = client_socket.recv(1024)
    print(response.decode())
except socket.error as e:
    print(f"Socket error: {e}")

client_socket.close()