import socket
import logging
import traceback
import threading
from typer import prompt
from .socket_base import MySocket


class Client(MySocket):
    BUFFER_SIZE = 1024

    def __init__(self, host, port, username) -> None:
        super().__init__()
        self.server_addr = (host, port)
        self.username = username
        self.send_thread= threading.Thread(target=self.send_messages) 
        self.recv_thread= threading.Thread(target=self.recv_messages) 
        self.send_thread.daemon = True; 
        self.recv_thread.daemon = True; 

    def connect_to_server(self):
        self.socket.connect(self.server_addr)
        self.socket.send(self.username.encode())
        print(f"\nConectado a {self.server_addr}...\n")
        self.socket.recv(self.BUFFER_SIZE)

    def disconnect(self):
        print("Desconectando...")
        self.socket.send("quit".encode())
        self.socket.close();
        self.send_thread.join()
        self.recv_thread.join()
        print("Desconexion completada...")

    def send_messages(self):
        while self.is_active:
            msg = str(prompt("->"))
            self.socket.send(msg.encode())
            if(msg == quit):
                self.is_active = False
                break

    def recv_messages(self):
        while self.is_active: #True:
            try:
                # if not self.send_thread.is_alive():
                #     break
                msg = self.socket.recv(self.BUFFER_SIZE).decode()
                print(self.is_active)
                print(f"\nmsg:{msg}")
            except Exception:
                break


    def run(self):
        try:
            self.is_active = True
            self.connect_to_server()
            self.send_thread.start()
            self.recv_thread.start()
            self.send_thread.join()
            self.recv_thread.join()
        except Exception:
            logging.error(traceback.format_exc())
            self.socket.close()
        except KeyboardInterrupt:
            self.disconnect()
            print("\nInterrumpido...")

        print('Saliendo...')

# if __name__ == "__main__":
#     host = "127.0.0.1"
#     port = 12345
#     buffer_size = 1024

#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     username = str(input("Introduce un nombre de usuario: ->"))
#     print("Cliente TCP")
#     print(f"Conectando con host: {host}:{port}...")

#     s.connect((host, port))  # conectando con el servidor
#     s.send(username.encode())
#     print(s.recv(buffer_size))

#     while True:
#         mensaje = str(input("-> "))
#         s.send(mensaje.encode("utf-8"))  # envio mensaje

#         if mensaje.lower() == "quit":  # orden de desconexión
#             print("Cerrando...")
#             s.close()  # cerrando socket
#             break

#         data = s.recv(buffer_size)  # recepción respuesta
#         data = data.decode("utf-8")
#         print(f"Recibido: {data}")
