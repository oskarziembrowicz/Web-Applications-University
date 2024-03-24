import socket
import datetime
HOST = '127.0.0.1'
PORT = 2901

def check_msgA_syntax(txt):
    s = len(txt.split(";"))
    if s != 9:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpA" and tmp[1] == "ver" and tmp[3] == "srcip" and tmp[5] == "dstip" and tmp[7] == "type":
            try:
                ver = int(tmp[2])
                srcip = tmp[4]
                dstip = tmp[6]
                type = int(tmp[8])
                if ver == 4 and type == 6 and srcip == "212.182.24.27" and dstip == "192.168.0.2":
                    return "TAK"
                else:
                    return "NIE"
            except:
                return "NIE"
        else:
            return "BAD_SYNTAX"


def check_msgB_syntax(txt):
    s = len(txt.split(";"))
    if s != 7:
        return "BAD_SYNTAX"
    else:
        tmp = txt.split(";")
        if tmp[0] == "zad15odpB" and tmp[1] == "srcport" and tmp[3] == "dstport" and tmp[5] == "data":

            try:
                srcport = int(tmp[2])
                dstport = int(tmp[4])
                data = tmp[6]

                if srcport == 2900 and dstport == 47526 and data == "network programming is fun":
                    return "TAK"
                else:
                    return "NIE"
            except:
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

client_socket, client_address = server_socket.accept()
print("Client connected")

while True:
    try:
        data = client_socket.recv(1024)
        print(f"Recieved a message: {data.decode()}")
        tokens = data.decode().split(';')
        if tokens[0] == "zad15odpA":
            output = check_msgA_syntax(data.decode())
        elif tokens[0] == "zad15odpB":
            output = check_msgB_syntax(data.decode())
        else:
            output = "BAD_SYNTAX"
        print(output)
        client_socket.send(output.encode())
    except:
        client_socket.close()

server_socket.close()