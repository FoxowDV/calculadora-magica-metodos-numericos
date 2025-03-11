from CustomWidgets import TitleLabel

from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from tabla import * 
import math


class MetodoBiseccion(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QGridLayout())

        #Creacion del titulo
        titulo = TitleLabel("Método de Biseccion")
        self.layout().addWidget(titulo, 0, 0, 1, 3)

        #Solicitud de los parametros requeridos para mi metodo
        letrerofuncion = QLabel("Funcion f(x)")
        letrerofuncion.setFont(QFont("Arial", 14))
        letrerofuncion.setStyleSheet("color: black")
        letrerofuncion.setFixedHeight(50)
        letrerofuncion.setAlignment(Qt.AlignHCenter)
        self.layout().addWidget(letrerofuncion, 1, 0, 1, 1) 

        letrerointervalo = QLabel("Intervalo [a,b] (f(a) < 0 < f(b))")
        letrerointervalo.setFont(QFont("Arial", 14))
        letrerointervalo.setStyleSheet("color: black")
        letrerointervalo.setFixedHeight(50)
        letrerointervalo.setAlignment(Qt.AlignHCenter)
        self.layout().addWidget(letrerointervalo, 1, 2, 1, 1)

        #Aqui se colocan los campos de entrada de texto
        self.entradafuncion = QLineEdit(self)
        self.entradafuncion.setStyleSheet("color: black;")
        self.entradaintervalo = QLineEdit(self)
        self.entradaintervalo.setStyleSheet("color: black;")
        
        self.layout().addWidget(self.entradafuncion, 2, 0, 1, 1)
        self.layout().addWidget(self.entradaintervalo, 2, 2, 1, 1)

        #Añadiendo los botones para mi metodo
        self.boton = QPushButton("Calcular", self)
        self.boton.clicked.connect(self.calcular)
        self.boton.setFixedSize(100, 40)
        self.boton.setStyleSheet("text-align: center; color: redblack; background-color: grey;")
        self.layout().addWidget(self.boton, 3, 0, 1, 1, alignment=Qt.AlignHCenter)

        self.boton = QPushButton("Calcular intervalo", self)
        self.boton.clicked.connect(self.comprobacion())
        self.boton.setFixedSize(100, 40)
        self.boton.setStyleSheet("text-align: center; color: redblack; background-color: grey;")
        self.layout().addWidget(self.boton, 3, 2, 1, 1, alignment=Qt.AlignHCenter)

        #Declaracion de la tabla
        

        self.layout().setColumnStretch(4, 0)

        self.hide()

    #Aqui se declara lo que sucede al pulsar el boton
    def comprobacion():
        self.entradafuncion.text()


    def calcular(self, intervalo_a: float, intervalo_b: float):

        intervaloaux=[intervalo_a, intervalo_b]

        ajusteIntervalo(intervaloaux)

        try:
            inicial = float(inicial)
        except ValueError: # Por si ponen texto
            print("Valor de 'inicial' no válido. Asegúrate de ingresar un número.")
            print(f"G(x): {funcion}, x_1: {inicial}") # Se muestran los valores que ingresamos en los inputs
        # Aqui voy a poner el metodo de aproximacion cuando lo termine
        #aprox_suc(inicial, 0.000000001, funcion)

 
    
           

    def validarIntervalo (intervaloaux,funcion_lam):
        
        aproxIzq = ["3","2","1"]
        aproxDer = ["2","4","6"]

        data = {
            'Intervalo <0': aproxIzq,
            'Intervalo >0': aproxDer
        }

        iteracion = 1

        a = intervaloaux[0]
        b = intervaloaux[1]

        while True:

            print("Iteracion [",iteracion,"]")

            c = eval(funcion_lam)
            d = eval(funcion_lam)
         
            if (c-d)<(0.0000000000000001):

                print("RAIZ ENCONTRADA: ",a)
                break

            elif (c * d) <= 0:
                intervaloaux = [a,resultado]
                print("Intervalo [",a,",",resultado,"] valido")
                aproxDer.append(resultado)
                aproxIzq.append(a)
            else:
                intervaloaux = [resultado,b]
                print("Intervalo [",resultado,",",b,"] valido")
                aproxDer.append(b)
                aproxIzq.append(resultado)

            iteracion+=1

            a = intervaloaux[0]
            b = intervaloaux[1]
            suma = a + b
            resultado = suma/2
    
        tabla = crear_tabla(data, self, 186)
        tabla.setFixedHeight(300)
        tabla.setFixedWidth(600)
        tabla.setStyleSheet("color: black;")
        self.layout().addWidget(tabla, 4, 0, 1, 3, alignment=Qt.AlignHCenter)