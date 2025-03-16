# Librerias del proyecto
import metodo_aprox, metodo_biseccion, metodo_newton, metodo_falsaPosicion
from CustomWidgets import SideBarButton, TitleLabel
import sys

# Librerias para hacer la GUI
from PySide6.QtWidgets import QApplication, QGridLayout, QWidget, QFrame
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Propieades de la ventana
        self.setFixedSize(900, 600)
        style = "background-color: #3a3a3a;color#ffffff; border-color: #051a39"
        self.setStyleSheet(style)


        # El frame principal está dividido en 2 Frames, el izquierdo y el derecho.
        # El frame izquierdo almacena el sidebar y siempre está visible. 
        # El frame derecho almacena el menu principal y cambia dependiendo del método seleccionado.
        # Ambos están almacenados dentro del layout de la ventana, a este se le refiere como main layout

        # Main layout
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0,0,0,0)


        # Contenedor izquierdo/sidebar
        sideBar = QFrame()
        sideBar.setFixedWidth(230)
        sideBar.setStyleSheet(style)

        sideBar.setLayout(QGridLayout())
        sideBar.layout().setContentsMargins(0,0,0,0)
        sideBar.layout().setAlignment(Qt.AlignTop)

        # Crear los botones del sidebar 
        # self.intervaloButton            = SideBarButton("Método de Intervalo")
        self.biseccionButton            = SideBarButton("Método de Bisección")
        self.aproxSucesivasButton       = SideBarButton("Método de Aproximación Sucesiva")
        self.interpolacionLinealButton  = SideBarButton("Método de Falsa Posición")
        self.newtonRaphsonButton        = SideBarButton("Método de Newton Raphson")


        # Añadir los botones al sidebar
        #sideBar.layout().addWidget(self.intervaloButton, 1, 0)
        sideBar.layout().addWidget(self.biseccionButton, 1, 0)
        sideBar.layout().addWidget(self.aproxSucesivasButton, 2, 0)
        sideBar.layout().addWidget(self.interpolacionLinealButton, 3, 0)
        sideBar.layout().addWidget(self.newtonRaphsonButton, 4, 0)
        
        # Añadir el sidebar al layout principal
        self.layout().addWidget(sideBar, 0, 0)


        # Contenedor derecho

        # Menu principal
        self.menuContainer = QFrame()
        self.menuContainer.setLayout(QGridLayout())

        title = TitleLabel("Calculadora magica de Métodos Númericos")
        self.menuContainer.layout().addWidget(title)

        # Metodo intervalo
        # self.containerMetodoIntervalo = QFrame() # NOTE: Cambiar cuando creen su archivo

        # Metodo biseccion
        self.containerMetodoBiseccion = metodo_biseccion.MetodoBiseccion() # NOTE: Cambiar cuando creen su archivo

        # Método aprox
        self.containerMetodoAprox = metodo_aprox.MetodoIntervalo()

        # Método interpolacion
        self.containerMetodoInterpolacion = metodo_falsaPosicion.MetodoFalsaPosicion()

        # Método newtonRaphson
        self.containerMetodoNewton = metodo_newton.MetodoNewtonRaphson()

        
        # Añadir los contenedores de los métodos al main layout
        self.layout().addWidget(self.menuContainer, 0, 1)
        # self.layout().addWidget(self.containerMetodoIntervalo, 0, 1)
        self.layout().addWidget(self.containerMetodoBiseccion, 0, 1)
        self.layout().addWidget(self.containerMetodoAprox, 0, 1)
        self.layout().addWidget(self.containerMetodoInterpolacion, 0, 1)
        self.layout().addWidget(self.containerMetodoNewton, 0, 1)


        # Conectar botones con sus correspondientes métodos
        self.biseccionButton.clicked.connect(self.showMetodoBiseccion)
        self.aproxSucesivasButton.clicked.connect(self.showMetodoAprox)
        self.interpolacionLinealButton.clicked.connect(self.showMetodoInterpolacion)
        self.newtonRaphsonButton.clicked.connect(self.showMetodoNewton)


    def showMetodoBiseccion(self):
        self.menuContainer.hide()
        self.containerMetodoAprox.hide()
        self.containerMetodoInterpolacion.hide()
        self.containerMetodoNewton.hide()

        self.containerMetodoBiseccion.show()

    def showMetodoAprox(self):
        self.menuContainer.hide()
        self.containerMetodoBiseccion.hide()
        self.containerMetodoInterpolacion.hide()
        self.containerMetodoNewton.hide()

        self.containerMetodoAprox.show()

    def showMetodoInterpolacion(self):
        self.menuContainer.hide()
        self.containerMetodoAprox.hide()
        self.containerMetodoBiseccion.hide()
        self.containerMetodoNewton.hide()

        
        self.containerMetodoInterpolacion.show()

    def showMetodoNewton(self):
        self.menuContainer.hide()
        self.containerMetodoAprox.hide()
        self.containerMetodoBiseccion.hide()
        self.containerMetodoInterpolacion.hide()

        self.containerMetodoNewton.show()





if __name__ == "__main__":
    # Creando aplicacion
    app = QApplication.instance()
    #inicializando ventana
    if app is None:
        app = QApplication(sys.argv)
    window = Window()
    # bucle principal
    window.show()
    sys.exit(app.exec())
