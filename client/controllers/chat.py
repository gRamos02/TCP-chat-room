import socket
from threading import Thread
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QMessageBox
from views.chat_ui import Ui_ChatForm

BUFFER_SIZE = 1024

class ChatWindow(QWidget, Ui_ChatForm):
    def __init__(self, username, address) -> None:
        super().__init__()
        self.setupUi(self)
        self.username = username
        self.address = address
        self.username_label.setText(f"Bienvenido, {username}")
        self.start_connection()
        self.send_button.clicked.connect(self.send_messages)

    def closeEvent(self, event) -> None:
        event.accept()
        self.exit()

    def start_connection(self) -> None:
        # address = ('localhost', 12345) #DATOS DEL SERVER
        self.client_socket = socket.socket(
            socket.AF_INET, # IPv4
            socket.SOCK_STREAM #TIPO (TCP)
        )
        #CONECTARSE Y MANDAR EL NOMBRE DE USUARIO
        self.client_socket.connect(self.address)
        self.client_socket.send(self.username.encode())

        recv_thread = Thread(target=self.recv_messages)
        recv_thread.daemon = True
        recv_thread.start()

    def exit(self):
        try:
            self.client_socket.send("quit".encode())
            self.client_socket.close()
        except Exception as err:
            print(err)

    def recv_messages(self) -> None:
        while True:
            try:
                message = self.client_socket.recv(BUFFER_SIZE).decode()
                self.msg_output.append(message)
                self.msg_output.setAlignment(Qt.AlignmentFlag.AlignLeft)
            except:
                self.exit()
                break
    
    def send_messages(self) -> None:
        message = self.msg_input.text()
        message = f"{self.username}: {message}"

        self.client_socket.send(message.encode())
        self.msg_output.append(message)
        self.msg_output.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.msg_input.clear()


    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_Return:
            self.send_messages() 
        else:
            super().keyPressEvent(event)
