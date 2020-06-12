import socket

server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_conn.connect(('127.0.0.1', 12800))
message_recv = server_conn.recv(1024)
print(message_recv.decode())
server_conn.close()