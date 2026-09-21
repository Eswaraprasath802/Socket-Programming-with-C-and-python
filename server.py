import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("172.30.22.244", 5000))

server.listen(1)

print("Waiting for client...")

conn, address = server.accept()

print("Client connected:", address)

data = conn.recv(1024)

print("Client says:", data.decode())

conn.sendall(b"Hello Client")

conn.close()
server.close()