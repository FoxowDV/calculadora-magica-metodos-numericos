from CustomWidgets import TitleLabel
from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from tabla import crear_tabla
import math
from functools import partial

class MetodoBiseccion(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QGridLayout())

        #linea provisional
        self.layout().setAlignment(Qt.AlignCenter)
        
        # Creación del título
        titulo = TitleLabel("Método de Bisección")
        self.layout().addWidget(titulo, 0, 0, 1, 4)

        # Etiquetas de parámetros
        self.agregarEtiqueta("Función f(x)", 1, 0)
        self.agregarEtiqueta("Intervalo [a,b] (f(a) < 0 < f(b))", 1, 2)

        # Campos de entrada
        self.entradafuncion = QLineEdit(self)
        self.entradaintervaloa = QLineEdit(self)
        self.entradaintervalob = QLineEdit(self)

        self.entradafuncion.setStyleSheet("text-align: center; color: black; background-color: grey;")
        self.entradaintervaloa.setStyleSheet("text-align: center; color: black; background-color: grey;")
        self.entradaintervalob.setStyleSheet("text-align: center; color: black; background-color: grey;")

        self.layout().addWidget(self.entradafuncion, 2, 0, 1, 2,alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.entradaintervaloa, 2, 2, 1, 1,alignment=Qt.AlignHCenter)
        self.layout().addWidget(self.entradaintervalob, 2, 3, 1, 1,alignment=Qt.AlignHCenter)

        # Botón para calcular
        self.boton = QPushButton("Calcular", self)
        self.boton.clicked.connect(lambda: self.comprobacion(self.entradafuncion.text(),
                                                             self.entradaintervaloa.text(),
                                                             self.entradaintervalob.text()))
        self.boton.setFixedSize(100, 40)
        self.boton.setStyleSheet("text-align: center; color: black; background-color: grey;")
        self.layout().addWidget(self.boton, 4, 0, 1, 1, alignment=Qt.AlignHCenter)

        self.layout().setColumnStretch(0, 1)
        self.layout().setColumnStretch(1, 1)
        self.layout().setColumnStretch(2, 1)
        self.layout().setColumnStretch(3, 1)
        self.layout().setColumnStretch(4, 1)
        self.hide()

    def agregarEtiqueta(self, texto, fila, columna):
        etiqueta = QLabel(texto)
        etiqueta.setFont(QFont("Arial", 14))
        etiqueta.setStyleSheet("color: black")
        etiqueta.setFixedHeight(50)
        etiqueta.setAlignment(Qt.AlignHCenter)
        self.layout().addWidget(etiqueta, fila, columna, 1, 1)

    def comprobacion(self, funcion, intaStr, intbStr):
        try:

            intervalo = [float(intaStr), float(intbStr)]
            print(funcion)
            self.calcular(intervalo, funcion)

        except ValueError:

            print(f"Error: Intervalo no válido '{intaStr}', '{intbStr}'")


    def calcular(self, intervalo, funcion_str):
        try:

            funcion = lambda x: eval(funcion_str, {"x": x, "math": math})
            self.validarIntervalo(intervalo, funcion)

        except Exception as e:
            print(f"Error al evaluar la función: {e}")


    def validarIntervalo(self, intervalo, funcion):
        aproxIzq = []
        aproxDer = []

        data = {
            'Intervalo <0': aproxIzq,
            'Intervalo >0': aproxDer
        }

        iteracion = 1
        
        while True:
            print(f"Iteración [{iteracion}]")

            varIz, varDer = intervalo

            varCen = (varIz + varDer) / 2

            try:
                resIz = funcion(varIz)
                resCen = funcion(varCen)
                resDer = funcion(varDer)

            except Exception as e:
                print(f"Error en la evaluación de la función: {e}")
                return

            if abs(resIz - resDer) <= 1e-15:
                print(f"RAÍZ ENCONTRADA: {varCen}")
                
                break

            elif resIz * resCen <= 0:

                intervalo = [varIz, varCen]

                print(f"Intervalo [{varIz}, {varCen}] válido")
                
                aproxIzq.append(str(varIz))
                aproxDer.append(str(varCen))
            
            elif resCen * resDer <= 0:
                
                intervalo = [varCen, varDer]

                print(f"Intervalo [{varCen}, {varDer}] válido")
                
                aproxIzq.append(str(varCen))
                aproxDer.append(str(varDer))

            iteracion += 1

        tabla = crear_tabla(data, self, 186)
        tabla.setFixedHeight(300)
        tabla.setFixedWidth(600)
        tabla.setStyleSheet("color: black;")
        self.layout().addWidget(tabla, 5, 0, 1, 4, alignment=Qt.AlignHCenter)
        self.agregarEtiqueta(f"RAIZ ENCONTRADA:{varCen}", 2, 0)