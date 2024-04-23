import socket

HOST = '127.0.0.1'
UDP_PORT = 2915
TCP_PORT = 2916

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, UDP_PORT))

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket.bind((HOST, TCP_PORT))
tcp_socket.listen(1)

while True:
    try:
        data, udp_client_address = udp_socket.recvfrom(4096)
        if data:
            print(f"Recieved a message: {data.decode()}")
            message = "You connected to UDP"
            print(f"Sending message: {message}")
            udp_socket.sendto(message.encode(), udp_client_address)
    except:
        udp_socket.close()

    tcp_client_socket, tcp_client_address = tcp_socket.accept()
    print("TCP Client connected")
    try:
        data = tcp_client_socket.recv(4096)
        if data:
            print(f"Recieved a message: {data.decode()}")
            message = "You connected to TCP"
            print(f"Sending message: {message}")
            tcp_client_socket.send(message.encode())
    except:
        tcp_client_socket.close()

udp_socket.close()
tcp_socket.close()