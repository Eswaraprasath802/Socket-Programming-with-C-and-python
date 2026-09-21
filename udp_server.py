import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("172.30.22.244", 5000))

print("Waiting for UDP message...")

data, address = server.recvfrom(1024)

print("Client:", address)
print("Client says:", data.decode())

server.sendto(b"Hello UDP Client", address)

server.close()