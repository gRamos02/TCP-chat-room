from PySide6.QtWidgets import QApplication
from controllers.login import LoginWindow
import sys

app = QApplication(sys.argv)
window = LoginWindow()

def run_client():
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run_client()