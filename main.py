# Librerias para hacer la GUI
import sys
from PySide6.QtWidgets import QApplication, QCheckBox, QGridLayout, QPushButton, QWidget, QTextEdit, QLabel, QFrame, QMenuBar
from PySide6.QtGui import QFont, QKeyEvent
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(900, 600)
        self.setMaximumSize(900, 600)
        self.setStyleSheet("background-color: red;margin=0")

        layout = QGridLayout(self)

        title = QLabel("Calculadora magica de Metodos Númericos")
        layout.addWidget(title, 0, 1)




        intervaloButton = QPushButton("Método de Intervalo")
        biseccionButton = QPushButton("Método de Bisección")
        aproxSucesivasButton = QPushButton("Método de Aproximación Sucesiva")
        interpolacionLinealButton = QPushButton("Método de Interpolación Lineal")
        newthonRaphsonButton = QPushButton("Método de Newton Raphson")

        buttonHeight = 35
        intervaloButton.setFixedHeight(buttonHeight)
        biseccionButton .setFixedHeight(buttonHeight)
        aproxSucesivasButton.setFixedHeight(buttonHeight)
        aproxSucesivasButton.setFixedHeight(buttonHeight)
        interpolacionLinealButton.setFixedHeight(buttonHeight)
        newthonRaphsonButton.setFixedHeight(buttonHeight)


        sideBar = QFrame()
        sideBar.setFixedWidth(230)
        sideBar.setFixedHeight(230)
        sideBar.setStyleSheet("background-color: gray; margin=0px")
        sideBarLayout = QGridLayout(sideBar)

        sideBarLayout.addWidget(intervaloButton, 1, 0)
        sideBarLayout.addWidget(biseccionButton, 2, 0)
        sideBarLayout.addWidget(aproxSucesivasButton, 3, 0)
        sideBarLayout.addWidget(interpolacionLinealButton, 4, 0)
        sideBarLayout.addWidget(newthonRaphsonButton, 5, 0)
        layout.addWidget(sideBar, 0, 0)






if __name__ == "__main__":
    # Creando aplicacion
    app = QApplication([])
    #inicializando ventana
    window = Window()
    # bucle principal
    window.show()
    sys.exit(app.exec())
