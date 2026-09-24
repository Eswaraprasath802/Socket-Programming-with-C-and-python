import socket
import struct
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432


def send_file(filepath):

    if not os.path.isfile(filepath):
        print("File does not exist.")
        return

    filename = os.path.basename(filepath)
    filename_bytes = filename.encode("utf-8")

    file_size = os.path.getsize(filepath)

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            client.settimeout(10)

            print(f"Connecting to {SERVER_HOST}:{SERVER_PORT}...")

            client.connect((SERVER_HOST, SERVER_PORT))

            print("Connected to server.")

            # -------------------------
            # Send filename length
            # -------------------------
            client.sendall(
                struct.pack("!I", len(filename_bytes))
            )

            # -------------------------
            # Send filename
            # -------------------------
            client.sendall(filename_bytes)

            # -------------------------
            # Send file size
            # -------------------------
            client.sendall(
                struct.pack("!Q", file_size)
            )

            # -------------------------
            # Send file data
            # -------------------------
            with open(filepath, "rb") as file:

                while True:

                    data = file.read(4096)

                    if not data:
                        break

                    client.sendall(data)

            print("File sent successfully.")

            # Tell server:
            # "I have finished sending."
            client.shutdown(socket.SHUT_WR)

            # -------------------------
            # Receive server response
            # -------------------------
            response = client.recv(1024)

            print("Server response:", response.decode("utf-8"))

    except ConnectionRefusedError:
        print("Connection refused. Is the server running?")

    except socket.timeout:
        print("Connection timed out.")

    except OSError as e:
        print(f"Network error: {e}")


if __name__ == "__main__":
    send_file("example.txt")