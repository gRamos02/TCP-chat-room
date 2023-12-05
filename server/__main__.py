from PySide6.QtWidgets import QApplication
from controllers.window import ServerWindow
import sys

app = QApplication(sys.argv)
window = ServerWindow(('0.0.0.0', 12345))

def run_client():
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run_client()