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
        username = self.username_input.text().lower()

        if username != '':
            from controllers.chat import ChatWindow
            self.chat_window = ChatWindow(username)
            self.chat_window.show()
            self.close()
        else:
            alert = QMessageBox(text='Introduce un nombre de usuario valido.')
            alert.exec()
            
