import socket

PORT = 5051
HEADER = 16
FORMAT = 'utf-8'
DISCONNECT_MSG = "End"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ADDR = (host_ip, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while True:
    msg = input("Enter message: ")
    if msg == DISCONNECT_MSG:
        send_msg(DISCONNECT_MSG)
        break
    send_msg(msg)

client.close()
