import socket
import threading

clients = {}
HOST = '127.0.0.1'
PORT = 8080

def handle_client(client_socket, client_name):
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                to_name, message = msg.split('|', 1)
                if to_name in clients:
                    clients[to_name].send(f"{client_name} dice: {message}".encode('utf-8'))
        except:
            print(f"{client_name} se desconectó")
            client_socket.close()
            del clients[client_name]
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        client_name = client_socket.recv(1024).decode('utf-8')
        clients[client_name] = client_socket
        print(f"{client_name} conectado desde {addr}")
        threading.Thread(target=handle_client, args=(client_socket, client_name)).start()

if __name__ == "__main__":
    start_server()

           