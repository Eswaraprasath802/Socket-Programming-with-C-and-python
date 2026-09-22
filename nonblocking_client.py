import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

print("1. Connected to server")

client.setblocking(False)

print("2. Client socket is NON-BLOCKING")

try:
    data = client.recv(1024)
    print("3. Received:", data.decode())

except BlockingIOError:
    print("3. No data available right now!")

client.sendall(b"Hello Server")

print("4. Data sent")

client.close()