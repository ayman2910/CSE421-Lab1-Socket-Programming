import socket

PORT = 5051
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
            conn.send("Goodbye".encode(FORMAT))
            break
        vowels = "aeiouAEIOU"
        count = 0
        for ch in msg:
            if ch in vowels:
                count += 1
        if count == 0:
            conn.send("Not enough vowels".encode(FORMAT))
        elif count <= 2:
            conn.send("Enough vowels I guess".encode(FORMAT))
        else:
            conn.send("Too many vowels".encode(FORMAT))

conn.close()
server.close()
