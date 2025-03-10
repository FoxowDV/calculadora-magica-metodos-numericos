# 
from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QFont

class MetodoNewtonRaphson(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QGridLayout())





    def calcularMetodo(self, x, fx, dfx, error):
        it = 1

        while (True):
            xp = x

            # Metodo de Newton Raphson
            x = x - (fx(x)/dfx(x))

            print(f"x{it}:", x)

            if (abs(x-xp) < error):
                break
            it+=1

