import socket
import datetime
HOST = '127.0.0.1'
PORT = 2901

def check_msg_syntax(txt):
    s = len(txt.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad13odp" and tmp[1] == "src" and tmp[3] == "dst" and tmp[5] == "data":
            try:
                src_port = int(tmp[2])
                dst_port = int(tmp[4])
                data = tmp[6]
            except :
                return "BAD_SYNTAX:"
            if src_port == 2900 and dst_port == 35211 and data == "hello :)":
                return "TAK"
            else:
                return "NIE"
        else:
            return "BAD_SYNTAX"

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

print("Waiting for clients...")

connected_clients_sockets.append(server_socket)


while True:
    client_socket, client_address = server_socket.accept()
    print("Client connected")
    try:
        data = client_socket.recv(1024)
        print(f"Recieved a message: {data.decode()}")
        output = check_msg_syntax(data.decode())
        print(output)
        client_socket.send(output.encode())
    except:
        client_socket.close()

server_socket.close()