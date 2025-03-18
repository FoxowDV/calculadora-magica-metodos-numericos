from CustomWidgets import InputField, TitleLabel, TextLabel, Button

# Esta es una clase que sirve como herencia entre el main y el frame de nuestro metodo

from PySide6.QtWidgets import QFrame, QGridLayout
from PySide6.QtCore import Qt
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
    self.layout().addWidget(labelX, 1, 1, 1, 1) # Inicia en la columna 1 y ocupa 1 columna en la fila 1

    # Creamos las cajas de texto donde se ingresaran los valores que se usaran en el metodo
    self.input1 = InputField(self)
    self.input2 = InputField(self)
    # Las agregamos al grid
    self.layout().addWidget(self.input1, 2, 0)
    self.layout().addWidget(self.input2, 2, 1)

    # Creamos el boton y lo agregamos en la fila 3, columna 0, ocupando 3 columnas
    self.boton = Button("Calcular", self)
    self.boton.clicked.connect(self.calcular)
    self.boton.setFixedSize(100, 40)
    self.layout().addWidget(self.boton, 3, 0, 1, 3, alignment=Qt.AlignHCenter)

    self.tablaWidget = Tabla(["Valor actual","Resultado", "Error"])
    self.layout().addWidget(self.tablaWidget, 4, 0, 1, 3)

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

      """
      El método de aproximación sucesiva usa una función iterativa xn+1=f(xn) 
      para generar una secuencia de valores que convergen a la solución deseada, 
      deteniéndose cuando la diferencia entre iteraciones es menor que un error predefinido.

      Se siguen los pasos:
      Evalúa la función func en x usando eval().
      Devuelve el valor de la función en x.
      Comienza con x como valor inicial.
      Itera hasta que la diferencia entre x y xn sea menor que error
      """

      print(f"Iteración {it}: x = {xn}")
      print(f"Error: x = {porcentaje_error}")
      self.tablaWidget.add_row([x, xn, error_formateado])
      
      if abs(x - xn) < error:
          print(f"Resultado final: {xn}")
          break
                
      x = xn
      it += 1
