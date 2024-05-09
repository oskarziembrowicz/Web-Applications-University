import socket, threading

HOST = '127.0.0.1'
PORT = 2901

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

lock = threading.Lock()
f = open("zad2serverLog.txt", "w")

print("Server is listening")

def serve(client, client_address):
    lock.acquire()
    try:
        data = client.recv(4096)
        if data:
            client.send(data)
            msg_success = f'Sending data to: {client_address}'
            print(msg_success)
            f.write(msg_success)
    except:
        msg_fail = f'Disconnected from client {client_address}'
        print(msg_fail)
        f.write(msg_fail)
        client.close()
    lock.release()

while True:

        client, client_address = server_socket.accept()
        print(f'Connected to client: {client_address}')
        threading.Thread(target=serve, args=(client, client_address)).start()
server_socket.close()