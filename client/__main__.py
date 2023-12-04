from PySide6.QtWidgets import QApplication
from controllers.login import LoginWindow
import sys

app = QApplication(sys.argv)
window = LoginWindow()

if __name__ == '__main__':
    window.show()
    sys.exit(app.exec())