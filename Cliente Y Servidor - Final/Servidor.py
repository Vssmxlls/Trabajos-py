import socket
import threading

def repeticion_cliente(conn, addr):
    print(f"La conexión se ha establecido correctamente con {addr}")
    conn.sendall("Bienvenido, para salir del servidor escribe 'salir'".encode())

    while True:
        data = conn.recv(1024)
        if not data:
            break

        mensaje = data.decode().strip()
        print(f"Mensaje recibido de {addr}: {mensaje}")

        if mensaje.lower() == "salir":
            print(f"El cliente con dirección {addr} se desconectó.")
            conn.sendall("Desconexión exitosa. Adiós.\n".encode())
            break

        respuesta = f"Mensaje recibido: {mensaje}\n"
        conn.sendall(respuesta.encode())

    conn.close()


HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=repeticion_cliente, args=(conn, addr))
        thread.start()

           