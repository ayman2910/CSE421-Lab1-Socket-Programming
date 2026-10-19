import socket

PORT = 5053
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
        hours = int(msg)
        if hours <= 40:
            salary = hours * 200
        else:
            salary = 8000 + (hours - 40) * 300
        conn.send(f"Salary: Tk {salary}".encode(FORMAT))

conn.close()
server.close()
