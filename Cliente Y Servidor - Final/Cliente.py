import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

import threading
import socket

class ClienteConThreading:
    def __init__(self, servidor_ip, servidor_puerto):
        self.servidor_ip = servidor_ip
        self.servidor_puerto = servidor_puerto
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.servidor_ip, self.servidor_puerto))
        self.hilo_recepcion = None
        self.hilo_envio = None 

    def iniciar_hilos(self):
        self.hilo_recepcion = threading.Thread(target=self.recibir_mensajes)
        self.hilo_recepcion.daemon = True  
        self.hilo_recepcion.start()

        self.hilo_envio = threading.Thread(target=self.enviar_mensajes)
        self.hilo_envio.daemon = True
        self.hilo_envio.start()

    def recibir_mensajes(self):
        while True:
            try:
                mensaje = self.socket.recv(1024).decode("utf-8")
                if not mensaje:
                    print("Desconectado del servidor.")
                    break
                print(f"Mensaje recibido: {mensaje}")
            except:
                print("Error al recibir mensaje. Se cierra la conexión.")
                break

    def enviar_mensajes(self):
        while True:
            try:
                mensaje = input("Ingrese mensaje (o 'salir' para desconectar): ")
                if mensaje.lower() == "salir":
                    self.socket.close()
                    break
                self.socket.sendall(mensaje.encode("utf-8"))
            except:
                print("Error al enviar mensaje. Se cierra la conexión.")
                break

ip_servidor = "127.0.0.1"  
puerto_servidor = 8080 
cliente = ClienteConThreading(ip_servidor, puerto_servidor)
cliente.iniciar_hilos()


 

