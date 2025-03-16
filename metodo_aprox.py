from CustomWidgets import InputField, TitleLabel, TextLabel, Button

# Esta es una clase que sirve como herencia entre el main y el frame de nuestro metodo

from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt #Esta perra mamada la tuve que sacar porque resulta que aqui estan los text-align para el Grid
from CustomWidgets import TitleLabel, Tabla

class MetodoIntervalo(QFrame):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setLayout(QGridLayout())

    # Fila 1: Título, centrado, copie y pegue lo del dani
    titulo = TitleLabel("Método de Aproximación Sucesiva")
    self.layout().addWidget(titulo, 0, 0, 1, 3)

    # Fila 2: Múltiples columnas, deje este para indicarle al usuario que cosas van en cada input
    labelGx = TextLabel("Ingrese la funcion igualada a x (g(x))")
    self.layout().addWidget(labelGx, 1, 0, 1, 1) # Inicia en la columna 0 y ocupa 2 columnas en la fila 1

    labelX = TextLabel("Valor de x")
    labelX.setAlignment(Qt.AlignHCenter)
    self.layout().addWidget(labelX, 1, 1, 1, 1) # Inicia en la columna 1 y ocupa 1 columna en la fila 1, hice un chingo de cambios hasta llegar a este resultado, no entiendo del todo como funciona el Grid layout

    # Creamos las cajas de texto donde se ingresaran los valores que se usaran en el metodo
    self.input1 = InputField(self)
    self.input2 = InputField(self)
    # Las agregamos al grid
    self.layout().addWidget(self.input1, 2, 0, 1, 2)
    self.layout().addWidget(self.input2, 2, 1, 1, 1)

    # Creamos el boton y lo agregamos en la fila 3, columna 0, ocupando 3 columnas
    self.boton = Button("Calcular", self)
    self.boton.clicked.connect(self.calcular)
    self.boton.setFixedSize(100, 40)
    self.layout().addWidget(self.boton, 3, 0, 1, 3, alignment=Qt.AlignHCenter)

    self.tablaWidget = Tabla(["Valor actual","Resultado", "Error"])
    self.layout().addWidget(self.tablaWidget, 4, 0, 1, 3)

    #Ahora si esto me dejo desconcertado, aparentemente se tiene que asignarles al fakin layout que no se estiren en caso de que hayan mas elementos en la fakin fila, hijos de la verga, estuve chinge y chinge con que se podia resolver de otras formas hasta que encontre esta funcion de un pinche sitio salido de la mano de dios, aunque ps eso me pasa por no saber usar StackOverflow
    self.layout().setColumnStretch(1, 0)
    self.layout().setColumnStretch(2, 0)

    self.hide()
  
  # Este es el metodo que se usa al pulsar el boton
  def calcular(self):
    funcion = self.input1.text()
    inicial = self.input2.text()
    # Convierte inicial al tipo de dato float para que lo pueda usar en el metodo
    try:
      inicial = float(inicial)
    except ValueError: # Por si ponen texto
      print("Valor de 'inicial' no válido. Asegúrate de ingresar un número.")
    print(f"G(x): {funcion}, x_1: {inicial}")
    aprox_suc(self, inicial, 0.000000001, funcion)

def fx(x, func):
  return eval(func)

def aprox_suc(self, x, error, func):
  self.tablaWidget.setRowCount(0)
  it = 1
  while True:
    xn = fx(x, func)
    if xn != 0:
      porcentaje_error = abs(xn - x) * 100
      error_formateado = f"{porcentaje_error}%"

      print(f"Iteración {it}: x = {xn}")
      print(f"Error: x = {porcentaje_error}")
      self.tablaWidget.add_row([x, xn, error_formateado])
      
      if abs(x - xn) < error:
          print(f"Resultado final: {xn}")
          break
                
      x = xn
      it += 1
