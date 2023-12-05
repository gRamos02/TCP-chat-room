from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QWidget, QMessageBox
from views.login_ui import Ui_LoginForm

class LoginWindow(QWidget, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_button.clicked.connect(self.login)

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_Return:
            self.login() 
        else:
            super().keyPressEvent(event)

    def login(self):
        try:
            addr = self.address_input.text()
            port = self.port_input.text()
            username = self.username_input.text().lower()
            if username == '' or addr == '' or port == '':
                alert = QMessageBox(text='Llena todo los campos')
                alert.exec()
            else:
                from controllers.chat import ChatWindow
                address = (addr, int(port))
                self.chat_window = ChatWindow(username, address)
                self.chat_window.show()
                self.close()
        except Exception as err:
            alert = QMessageBox(text=f"{err}")
            alert.exec()
            
