import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall()
  data = s.recv(1024)

print("Señal por parte del servidor recibida",repr(data))
