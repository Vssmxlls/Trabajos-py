import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class ChatClient:
    def __init__(self, root, name, target_name):
        self.name = name
        self.target_name = target_name

        self.root = root
        self.root.title(f"Cliente {name}")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Encabezado azul
        header = tk.Label(root, text=f"Cliente {name}", bg="#2E8BC0", fg="white", font=("Arial", 12, "bold"))
        header.pack(fill=tk.X)

        # Área de mensajes
        self.text_area = scrolledtext.ScrolledText(root, width=40, height=15, font=("Arial", 10))
        self.text_area.pack(pady=10)
        self.text_area.config(state='disabled')

        # Entrada de mensaje
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)

        self.msg_entry = tk.Entry(input_frame, width=20, font=("Arial", 10))
        self.msg_entry.pack(side='left', padx=(10, 5))
        self.msg_entry.bind("<Return>", lambda event: self.send_message())

        self.send_button = tk.Button(input_frame, text="Enviar", command=self.send_message)
        self.send_button.pack(side='left')

        # Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 8080))
        self.sock.send(self.name.encode('utf-8'))

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self):
        msg = self.msg_entry.get().strip()
        if msg:
            message_to_send = f"{self.target_name}|{msg}"
            self.sock.send(message_to_send.encode('utf-8'))
            self.update_chat(f"Tú: {msg}")
            self.msg_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                msg = self.sock.recv(1024).decode('utf-8')
                self.update_chat(msg)
            except:
                break

    def update_chat(self, msg):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, msg + '\n')
        self.text_area.config(state='disabled')
        self.text_area.see(tk.END)

if __name__ == "__main__":
    name = input("Tu nombre (ej. Paty o Javi): ")
    target = input("Enviar mensajes a (ej. Javi o Paty): ")
    root = tk.Tk()
    app = ChatClient(root, name, target)
    root.mainloop()