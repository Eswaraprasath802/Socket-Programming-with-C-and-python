import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 5000))

while True:
    data = sock.recv(2)

    if not data:
        break

    print("Process immediately:", data)

sock.close()