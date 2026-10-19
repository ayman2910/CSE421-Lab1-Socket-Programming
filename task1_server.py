import socket

PORT = 5050
HEADER = 16
FORMAT = 'utf-8'
DISCONNECT_MSG = "End"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ADDR = (host_ip, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("Server is listening on", ADDR)

conn, addr = server.accept()
print("Connected from", addr)
connected = True
while connected:
    msg_len = conn.recv(HEADER).decode(FORMAT)
    if msg_len:
        msg_len = int(msg_len)
        msg = conn.recv(msg_len).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
            conn.send("Disconnected".encode(FORMAT))
        else:
            print(msg)
            conn.send("Client info received".encode(FORMAT))

conn.close()
server.close()
