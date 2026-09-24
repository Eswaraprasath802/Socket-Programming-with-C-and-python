import socket
import struct
import os

HOST = "0.0.0.0"
PORT = 65432
BUFFER_SIZE = 4096
SAVE_DIR = "received_files"


def receive_exact(conn, size):
    data = b""

    while len(data) < size:
        chunk = conn.recv(size - len(data))

        if not chunk:
            raise ConnectionError("Connection closed while receiving data")

        data += chunk

    return data


def start_server():
    os.makedirs(SAVE_DIR, exist_ok=True)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server.bind((HOST, PORT))
        server.listen(5)

        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()

            with conn:
                print(f"Client connected: {addr}")

                try:
                    # -------------------------
                    # Receive filename length
                    # -------------------------
                    filename_length_data = receive_exact(conn, 4)
                    filename_length = struct.unpack("!I", filename_length_data)[0]

                    # -------------------------
                    # Receive filename
                    # -------------------------
                    filename_data = receive_exact(conn, filename_length)
                    filename = filename_data.decode("utf-8")

                    filename = os.path.basename(filename)
                    filepath = os.path.join(SAVE_DIR, filename)

                    # -------------------------
                    # Receive file size
                    # -------------------------
                    file_size_data = receive_exact(conn, 8)
                    file_size = struct.unpack("!Q", file_size_data)[0]

                    print(f"Receiving: {filename}")
                    print(f"File size: {file_size} bytes")

                    # -------------------------
                    # Receive file
                    # -------------------------
                    received = 0

                    with open(filepath, "wb") as file:
                        while received < file_size:

                            remaining = file_size - received
                            chunk_size = min(BUFFER_SIZE, remaining)

                            data = conn.recv(chunk_size)

                            if not data:
                                raise ConnectionError(
                                    "Connection closed during file transfer"
                                )

                            file.write(data)
                            received += len(data)

                    print(f"File received successfully: {filepath}")

                    # -------------------------
                    # Send response
                    # -------------------------
                    conn.sendall(b"FILE_RECEIVED")

                except ConnectionError as e:
                    print(f"Connection error: {e}")

                except OSError as e:
                    print(f"Network error: {e}")

                except Exception as e:
                    print(f"Unexpected error: {e}")


if __name__ == "__main__":
    start_server()