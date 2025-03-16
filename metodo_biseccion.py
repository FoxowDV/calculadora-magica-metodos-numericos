from CustomWidgets import Button, InputField, TextLabel, TitleLabel, Tabla

import math
from typing import Callable
 
from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QLineEdit

class MetodoBiseccion(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QGridLayout())
        
        # Creación del título
        titulo = TitleLabel("Método de Bisección")
        self.layout().addWidget(titulo)

        # Etiquetas de parámetros
        self.layout().addWidget(TextLabel("Función f(x)"))
        

        # Campos de entrada
        entradafuncion      = InputField(self)
        entradaintervaloa   = InputField(self)
        entradaintervalob   = InputField(self)

        self.layout().addWidget(entradafuncion)
        self.layout().addWidget(TextLabel("Extremo izquierdo del intervalo [a, f(a) < 0 "))
        self.layout().addWidget(entradaintervaloa)
        self.layout().addWidget(TextLabel("Extremo derecho del intervalo ,b] 0 < f(b)"))
        self.layout().addWidget(entradaintervalob)

        # Botón para calcular

        calcularButton = Button("Calcular")
        self.layout().addWidget(calcularButton)

        self.tablaWidget = Tabla(["Resultado", "Limite"])
        self.layout().addWidget(self.tablaWidget)

        calcularButton.clicked.connect(lambda: self.comprobacion(entradafuncion.text(),
                                                             entradaintervaloa.text(),
                                                             entradaintervalob.text()))

        self.hide()

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

            if abs(resIz - resDer) <= 0.01:
                print(f"RAÍZ ENCONTRADA: {varCen}")
                
                break

            elif resIz * resCen <= 0:

                intervalo = [varIz, varCen]

                print(f"Intervalo [{varIz}, {varCen}] válido")
                
                self.tablaWidget.add_row([varIz, varCen])
            
            elif resCen * resDer <= 0:
                
                intervalo = [varCen, varDer]

                print(f"Intervalo [{varCen}, {varDer}] válido")
                
                self.tablaWidget.add_row([varCen, varDer])

            iteracion += 1

        self.tablaWidget.add_row(["Resultado", varDer])
