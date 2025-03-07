# Librerias para hacer la GUI
import sys
from PySide6.QtWidgets import QApplication, QCheckBox, QGridLayout, QPushButton, QWidget, QTextEdit, QLabel, QFrame, QMenuBar
from PySide6.QtGui import QFont, QKeyEvent
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Propieades de la ventana
        self.setMinimumSize(900, 600)
        self.setMaximumSize(900, 600)
        self.setStyleSheet("background-color: #ffffff;")

        font = QFont("Arial", 14)
        self.setFont(font)

        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0,0,0,0)


        # Contenedor de la menu principal
        self.containerPrincipal = QFrame()
        self.containerLayout = QGridLayout(self.containerPrincipal)

        title = QLabel("Calculadora magica de Metodos Númericos")
        title.setFont(QFont("Arial", 26))
        self.containerLayout.addWidget(title)


        # Contenedor metodo intervalo
        self.containerMetodoIntervalo = QFrame()
        self.containerMetodoIntervalo.hide()
        self.containerMetodoIntervaloLayout = QGridLayout(self.containerMetodoIntervalo)

        textouwu1 = QLabel("Metodo de intervalo")
        textouwu1.setFont(QFont("Arial", 26))
        self.containerMetodoIntervaloLayout.addWidget(textouwu1)


        # Contenedor metodo biseccion
        self.containerMetodoBiseccion = QFrame()
        self.containerMetodoBiseccion.hide()
        self.containerMetodoBiseccionLayout = QGridLayout(self.containerMetodoBiseccion)

        textouwu1 = QLabel("Metodo de b")
        textouwu1.setFont(QFont("Arial", 26))
        self.containerMetodoBiseccionLayout.addWidget(textouwu1)



        # Contenedor metodo aprox
        self.containerMetodoAprox = QFrame()
        self.containerMetodoAprox.hide()
        self.containerMetodoAproxLayout = QGridLayout(self.containerMetodoAprox)

        textouwu1 = QLabel("Metodo de aprox")
        textouwu1.setFont(QFont("Arial", 26))
        self.containerMetodoAproxLayout.addWidget(textouwu1)



        # Contenedor metodo interpolacion
        self.containerMetodoInterpolacion = QFrame()
        self.containerMetodoInterpolacion.hide()
        self.containerMetodoInterpolacionLayout = QGridLayout(self.containerMetodoInterpolacion)

        textouwu1 = QLabel("Metodo de inter")
        textouwu1.setFont(QFont("Arial", 26))
        self.containerMetodoInterpolacionLayout.addWidget(textouwu1)



        # Contenedor metodo newtonRaphson
        self.containerMetodoNewton = QFrame()
        self.containerMetodoNewton.hide()
        self.containerMetodoNewtonLayout = QGridLayout(self.containerMetodoNewton)

        textouwu1 = QLabel("Metodo de newton")
        textouwu1.setFont(QFont("Arial", 26))
        self.containerMetodoNewtonLayout.addWidget(textouwu1)


        

        # Botones del menu
        self.intervaloButton = QPushButton("Método de Intervalo")
        self.biseccionButton = QPushButton("Método de Bisección")
        self.aproxSucesivasButton = QPushButton("Método de Aproximación Sucesiva")
        self.interpolacionLinealButton = QPushButton("Método de Interpolación Lineal")
        self.newtonRaphsonButton = QPushButton("Método de Newton Raphson")

        buttonHeight = 35
        self.intervaloButton.setFixedHeight(buttonHeight)
        self.biseccionButton.setFixedHeight(buttonHeight)
        self.aproxSucesivasButton.setFixedHeight(buttonHeight)
        self.aproxSucesivasButton.setFixedHeight(buttonHeight)
        self.interpolacionLinealButton.setFixedHeight(buttonHeight)
        self.newtonRaphsonButton.setFixedHeight(buttonHeight)


        
        # Contenedor de la izquierda
        sideBar = QFrame()
        sideBar.setFixedWidth(230)
        sideBar.setStyleSheet("background-color: #ebeded;")

        sideBarLayout = QGridLayout(sideBar)
        sideBarLayout.setContentsMargins(0,0,0,0)

        sideBarLayout.addWidget(self.intervaloButton, 1, 0)
        sideBarLayout.addWidget(self.biseccionButton, 2, 0)
        sideBarLayout.addWidget(self.aproxSucesivasButton, 3, 0)
        sideBarLayout.addWidget(self.interpolacionLinealButton, 4, 0)
        sideBarLayout.addWidget(self.newtonRaphsonButton, 5, 0)


        self.layout.addWidget(sideBar, 0, 0)
        self.layout.addWidget(self.containerPrincipal, 0, 1)
        self.layout.addWidget(self.containerMetodoIntervalo, 0, 1)
        self.layout.addWidget(self.containerMetodoBiseccion, 0, 1)
        self.layout.addWidget(self.containerMetodoAprox, 0, 1)
        self.layout.addWidget(self.containerMetodoInterpolacion, 0, 1)
        self.layout.addWidget(self.containerMetodoNewton, 0, 1)

        self.intervaloButton.clicked.connect(self.showMetodoIntervalo)
        self.biseccionButton.clicked.connect(self.showMetodoBiseccion)
        self.aproxSucesivasButton.clicked.connect(self.showMetodoAprox)
        self.interpolacionLinealButton.clicked.connect(self.showMetodoInterpolacion)
        self.newtonRaphsonButton.clicked.connect(self.showMetodoNewton)


    def showMetodoIntervalo(self):
        self.containerPrincipal.hide()
        self.containerMetodoIntervalo.show()

    def showMetodoBiseccion(self):
        self.containerPrincipal.hide()
        self.containerMetodoBiseccion.show()

    def showMetodoAprox(self):
        self.containerPrincipal.hide()
        self.containerMetodoAprox.show()

    def showMetodoInterpolacion(self):
        self.containerPrincipal.hide()
        self.containerMetodoInterpolacion.show()

    def showMetodoNewton(self):
        self.containerPrincipal.hide()
        self.containerMetodoNewton.show()





if __name__ == "__main__":
    # Creando aplicacion
    app = QApplication([])
    #inicializando ventana
    window = Window()
    # bucle principal
    window.show()
    sys.exit(app.exec())
