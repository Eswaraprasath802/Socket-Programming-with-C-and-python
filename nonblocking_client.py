import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

print("Client connected.")
input("Press ENTER to send data...")

client.sendall(b"Hello Server")

client.close()