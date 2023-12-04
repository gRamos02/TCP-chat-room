from typing import Optional
from PySide6.QtCore import Qt, QThread
from PySide6.QtWidgets import QWidget, QMessageBox
from views.server_ui import Ui_ServerForm 
from enum import Enum
import socket
import logging
import traceback
from threading import Thread

#ENUM para representar el estado del server
class Status(Enum):
    OFF = 0
    ON = 1 


BUFFER_SIZE = 1024

#Clase del hilo donde corre el servidor (pa probar QThread)
class ServerThread(QThread):
    def __init__(self, server_window) -> None:
        super().__init__()
        self.server_window = server_window

    def run(self):
        self.server_window.status = Status.ON 
        print(f"Servidor inicializado en {self.server_window.address}\nEsperando conexiones...")
        self.server_window.server_console.append(f"Servidor inicializado en {self.server_window.address}\nEsperando conexiones...")
        # while True:
        while self.server_window.status == Status.ON:
            try:
                client, addr = self.server_window.accept_connection()
                self.server_window.msg_thread = Thread(target=self.server_window.process_messages, args=(client,))
                self.server_window.msg_thread.daemon = True
                self.server_window.msg_thread.start()
            except OSError:
                self.server_window.shutdown_server()
                logging.error(traceback.format_exc())
                self.server_window.server_console.append(traceback.format_exc())
            except KeyboardInterrupt:
                self.server_window.shutdown_server()
                print("Se interrumpio el servidor")
                self.server_window.server_console.append("Se interrumpio el servidor...")
            except Exception:
                self.server_window.shutdown_server()
                logging.error(traceback.format_exc())
                self.server_window.server_console.append(traceback.format_exc())

        self.server_window.msg_thread.join()
        


#Clase de la ventana
class ServerWindow(QWidget, Ui_ServerForm):
    connected_clients = []
    usernames = []

    def __init__(self, address) -> None:
        super().__init__()
        self.setupUi(self)
        self.status = Status.OFF
        self.address = address
        self.server_button.clicked.connect(self.run_server)
        self.socket = socket.socket(
            socket.AF_INET, # IPv4
            socket.SOCK_STREAM #TIPO (TCP)
        )
        try:
            self.socket.bind(self.address)
            self.socket.listen(1)
        except OSError as err:
            if err.errno == 98:
                print("La direccion ya esta en uso")
                self.server_console.append("La direccion ya esta en uso")
                self.socket.close()
        self.server_thread = ServerThread(self)

    def closeEvent(self, event) -> None:
        if self.server_thread.isRunning():
            self.shutdown_server()
        else:
            event.accept()
        exit()

    def run_server(self):
        self.server_thread.start()
       
    def accept_connection(self):
        #Aceptar la conexion, regresar socket y direccion del cliente
        client, addr = self.socket.accept()
        #Guardar el usuario seleccionado en el cliente
        # Y tambien guardar el socket en sus respectivas listas
        username = client.recv(BUFFER_SIZE).decode()
        self.connected_clients.append(client)
        self.usernames.append(username)
        print(f"{username} conectado desde: {str(addr)}")
        self.server_console.append(f"{username} conectado desde: {str(addr)}")
        client.send(f"Server: Bienvenido, {username}".encode())
        self.send_message(f"{username} se ha unido...".encode(), client)
        return (client, addr)
    
    def process_messages(self, client):
        while self.status == Status.ON:
            try:
                msg = client.recv(BUFFER_SIZE)
                if(msg.decode().lower() == "quit"):
                    self.disconnect_client(client)
                    break

                self.send_message(msg, client)
            except:
                self.disconnect_client(client)
                logging.error(traceback.format_exc())
                self.server_console.append(traceback.format_exc())
                break

    def disconnect_client(self, client):
        idx = self.connected_clients.index(client)
        username = self.usernames[idx]
        self.send_message(f"Server: {username} se desconecto...".encode(), client)
        self.connected_clients.remove(client)
        self.usernames.remove(username)
        client.close()
        print(f"Se desconecto el usuario {username}")
        self.server_console.append(f"Se desconecto el usuario {username}")

    def send_message(self, message, __client):
        #Por cada cliente conectado se enviara el mensaje (ya codificado)
        for client in self.connected_clients:
            #A todos menos el emisor
            if client != __client:
                client.send(message)

    def shutdown_server(self):
        print("Apagando server...")
        self.status = Status.OFF
        self.server_console.append("Apagando servidor...")
        self.socket.close()
        print("Apagado...")
        self.server_console.append("El servidor ha sido apagado...")