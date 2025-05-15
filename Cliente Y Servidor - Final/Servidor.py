import socket 
import threading
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST,PORT))
    socket.listen()

    conn, addr = socket.accept()

    with conn:
        print(f"Conexion exitosa con el cliente",{addr})
        while True:
            data = conn.recv(1204)
            if not data: break
            conn.sendall(data)