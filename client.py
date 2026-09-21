import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("172.30.22.244", 5000))

client.sendall(b"Hello Server")

data = client.recv(1024)

print("Server says:", data.decode())

client.close()