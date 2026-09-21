import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(
    b"Hello UDP Server",
    ("172.30.22.244", 5000)
)

data, address = client.recvfrom(1024)

print("Server:", address)
print("Server says:", data.decode())

client.close()