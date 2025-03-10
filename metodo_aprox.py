# Esta es una clase que sirve como herencia entre el main y el frame de nuestro metodo

from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt #Esta perra mamada la tuve que sacar porque resulta que aqui estan los text-align para el Grid
from tabla import * # Importo lo de la tabla.py
#Intentare explicar cosas de la forma mas consisa posible y con los menos comentarios que pueda, pero ps a ver que pasa al final

#Esto es lo que invocamos desde el main.py, se declara como un QFrame para que ps sea un cuadro
#El primer metodo __init__ y la primera linea de ese metodo basicamente hacen que el cuadro pertenezca al QFrame del main
#Edit olvidendlo, lo llene de puro pinche texto
class MetodoIntervalo(QFrame):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setLayout(QGridLayout())

    # Fila 1: Título, centrado, copie y pegue lo del dani
    textouwu1 = QLabel("Metodo de Aproximacion Sucesiva")
    textouwu1.setFont(QFont("Arial", 26))
    textouwu1.setFixedHeight(50)
    textouwu1.setAlignment(Qt.AlignHCenter) #No se porque pero cuando lo pones como AlignCenter normal se expande el tamaño de la fila.
    self.layout().addWidget(textouwu1, 0, 0, 1, 3) #Asignado a la fila 0, columna 0, indicamos que es solo 1 columna e indicamos que va a ocupar el espacio de 3 columnas (es importante hacerlo asi para que en las siguientes columnas no se limite a una sola columna)

    # Fila 2: Múltiples columnas, deje este para indicarle al usuario que cosas van en cada input
    labelGx = QLabel("Ingrese la funcion igualada a x (g(x))")
    labelGx.setFont(QFont("Arial", 14))
    labelGx.setStyleSheet("color: black")
    labelGx.setFixedHeight(50)
    labelGx.setAlignment(Qt.AlignHCenter)
    self.layout().addWidget(labelGx, 1, 0, 1, 1) # Inicia en la columna 0 y ocupa 2 columnas en la fila 1

    labelX = QLabel("Valor de x")
    labelX.setFont(QFont("Arial", 14))
    labelX.setStyleSheet("color: black")
    labelX.setFixedHeight(50)
    labelX.setAlignment(Qt.AlignHCenter)
    self.layout().addWidget(labelX, 1, 1, 1, 1) # Inicia en la columna 1 y ocupa 1 columna en la fila 1, hice un chingo de cambios hasta llegar a este resultado, no entiendo del todo como funciona el Grid layout

    # Creamos las cajas de texto donde se ingresaran los valores que se usaran en el metodo
    self.input1 = QLineEdit(self)
    self.input2 = QLineEdit(self)
    # Las agregamos al grid
    self.layout().addWidget(self.input1, 2, 0, 1, 2)
    self.layout().addWidget(self.input2, 2, 1, 1, 1) #Un poco lo mismo aca, no entiendo como verga funciona el grid pero jala y se bonito

    # Creamos el boton y lo agregamos en la fila 3, columna 0, ocupando 3 columnas
    self.boton = QPushButton("Calcular", self)
    self.boton.clicked.connect(self.calcular) # Le asignamos el metodo que esta en la linea 63 para mostrar el resultado, recomiendo ver el metodo despues de leer como funciona la tabla
    self.boton.setFixedSize(100, 40)
    self.boton.setStyleSheet("text-align: center;")
    self.layout().addWidget(self.boton, 3, 0, 1, 3, alignment=Qt.AlignHCenter)

    # Crear vacio para la tabla y agregarla al layout, este es un muy buen momento para ir a ver como funciona el metodo crear_tabla, ahi explicare con mas detalle para que sirve cada valor que le asignamos
    # La razon por la que hago vacio es porque ps al principio no hay nada, ni una iteracion
    tabla = crear_tabla(data, self, 186) # Esta en el archivo tabla.py
    tabla.setFixedHeight(300)
    tabla.setFixedWidth(600)
    self.layout().addWidget(tabla, 4, 0, 1, 3, alignment=Qt.AlignHCenter)

    #Ahora si esto me dejo desconcertado, aparentemente se tiene que asignarles al fakin layout que no se estiren en caso de que hayan mas elementos en la fakin fila, hijos de la verga, estuve chinge y chinge con que se podia resolver de otras formas hasta que encontre esta funcion de un pinche sitio salido de la mano de dios, aunque ps eso me pasa por no saber usar StackOverflow
    self.layout().setColumnStretch(1, 0)
    self.layout().setColumnStretch(2, 0)

    self.hide()#Escondete puto
  
  # Este es el metodo que se usa al pulsar el boton
  def calcular(self):
    funcion = self.input1.text()
    inicial = self.input2.text()
    # Convierte inicial al tipo de dato float para que lo pueda usar en el metodo
    try:
      inicial = float(inicial)
    except ValueError: # Por si ponen texto
      print("Valor de 'inicial' no válido. Asegúrate de ingresar un número.")
    print(f"G(x): {funcion}, x_1: {inicial}") # Se muestran los valores que ingresamos en los inputs
    # Aqui voy a poner el metodo de aproximacion cuando lo termine
    #aprox_suc(inicial, 0.000000001, funcion)
    tabla = crear_tabla(data, self, 186) #Si no leiste lo anterior que puse, recomiendo leer el metodo en la clase tabla
    tabla.setFixedHeight(300)
    tabla.setFixedWidth(600)
    self.layout().addWidget(tabla, 4, 0, 1, 3, alignment=Qt.AlignHCenter)

# Ahora fuera de ese desmadre vamos a declarar cositas, esto se deberia de poner al inicio pero ps
# siento que es mas facil de entender de arriba hacia abajo

# Primero, estos arreglos, aqui vamos a guardar los valores que se van a mostrar en la tabla
# Se tienen que declarar arreglos en base a que tanto se va a mostrar, depende del metodo
x_actuales = [] # Valor de x actual, el primer valor de aqui es el que ingresamos en donde dice "Valor inicial", los siguientes son los resultados que se van haciendo en cada iteracion
resultados = [] # Ps se entiende, el ultimo es la raiz de la funcion
erRelPorcentuales = [] # Aqui se agregan los errores relativos porcentuales de cada iteracion

# Ahora declaramos un diccionario con los valores de los arreglos que hicimos
# Esto es lo que toma el metodo crear_tabla para hacer la tabla y ps lo que se va a mostrar
data = {
    'X_actual': x_actuales,
    'Resultado': resultados,
    'Error': erRelPorcentuales
}
