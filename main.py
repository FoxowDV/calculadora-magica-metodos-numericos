# Librerias para hacer la GUI
import sys
from PySide6.QtWidgets import QApplication, QCheckBox, QGridLayout, QPushButton, QWidget, QTextEdit, QLabel
from PySide6.QtGui import QFont, QKeyEvent
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)




if __name__ == "__main__":
    # Creando aplicacion
    app = QApplication([])
    #inicializando ventana
    window = Window()
    # bucle principal
    window.show()
    sys.exit(app.exec())
