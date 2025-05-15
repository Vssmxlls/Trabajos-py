import socket 
import threading

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()

    conn, addr = s.accept()

    with conn:
        print(f"Conexion exitosa con el cliente",{addr})
        while True:
            data = conn.recv(1204)
            if not data: break
            conn.sendall(data)