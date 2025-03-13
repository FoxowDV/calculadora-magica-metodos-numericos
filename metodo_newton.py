from CustomWidgets import TitleLabel
from tabla import crear_tabla


import math
from typing import Callable


# 
from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QFont


class MetodoNewtonRaphson(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QGridLayout())

        title = TitleLabel("Método de Newton Raphson")
        self.layout().addWidget(title)

        
        valueX = QLineEdit(self)
        valueFx= QLineEdit(self)
        valuedFx = QLineEdit(self)
        valueError = QLineEdit(self)

        
        self.layout().addWidget(QLabel("Valor de x"))
        self.layout().addWidget(valueX)
        self.layout().addWidget(QLabel("Valor de fx"))
        self.layout().addWidget(valueFx)
        self.layout().addWidget(QLabel("Valor de dfx"))
        self.layout().addWidget(valuedFx)
        self.layout().addWidget(QLabel("Error minimo"))
        self.layout().addWidget(valueError)

        calcularButton = QPushButton("Calcular")
        self.layout().addWidget(calcularButton)

        funcion = lambda x: eval(valueFx.text(), {"x":x, "math": math})
        derivadaFuncion = lambda x: eval(valuedFx.text(), {"x":x, "math": math})
        calcularButton.clicked.connect(
                lambda: self.calcularMetodoNewtonRapson(
                    float(valueX.text()),
                    funcion,
                    derivadaFuncion,
                    float(valueError.text()),
                )
            )
        self.valoresDeX = []
        self.errores = []

        self.hide()


    def calcularMetodoNewtonRapson(
            self, 
            x: float,
            fx: Callable, 
            dfx: Callable,
            error: float
            ) -> None:
        """
        El método de Newton Rapshon permite calcular la raíz de una función utilizando la idea
        de la aproximación lineal mediante iteraciones.

        La formula para calcular el méotodo es la siguiente:
        xn+1 = xn - (f(xn)/f'(xn))

        Durante cada iteración, el valor de x será cada vez más cercano al valor real de la raíz.

        Parametros
        ----------
        x       : Valor de tipo int que define el valor inicial de x, se recomienda empezar en 0.
        fx      : Función que define fx
        dfx     : Función que define la derivada de fx
        error   : Valor decimal que define el error 
        """

        it = 1
        while (True):
            xp = x

            # Metodo de Newton Raphson
            x = x - (fx(x)/dfx(x))

            
            # Guardar los resultado para mostrarlos, no afecta el funcionamiento
            self.valoresDeX.append(str(x))
            self.errores.append(str(abs(x-xp)))

            if (abs(x-xp) < error):
                break
            it+=1

        self.data = {
            "resultado": self.valoresDeX,
            "error": self.errores
        }
        tabla = crear_tabla(self.data, self, 300)
        self.layout().addWidget(tabla)


