from CustomWidgets import TitleLabel  
from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QLineEdit 
from PySide6.QtGui import QFont 
from PySide6.QtCore import Qt 
from tabla import crear_tabla 
# from CustomWidgets import Tabla  
import math  

# Definimos la clase del Método de Falsa Posición como el Wen
class MetodoFalsaPosicion(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)  # Llamamos al constructor de la clase padre QFrame
        self.setLayout(QGridLayout())  # Usamos un diseño de cuadrícula para organizar los elementos
        
        # Centramos todos los elementos dentro del layout
        self.layout().setAlignment(Qt.AlignCenter)

        # Fila 1: Título, centrado, copie y pegue lo del dani
        titulo = TitleLabel("Método de Falsa Posición")  
        self.layout().addWidget(titulo, 0, 0, 1, 4)  
        #Asignado a la fila 0, columna 0, indicamos que es solo 1 columna e indicamos que va a ocupar el espacio de 4 columnas 
         

        # Agregamos etiquetas para indicar qué valores debe ingresar el usuario
        self.agregarEtiqueta("Función f(x)", 1, 0)  # Texto para la función
        self.agregarEtiqueta("Intervalo [a, b]", 1, 2)  # Texto para los valores de a y b

        # Creamos los campos de entrada de texto para la función, a y b
        self.entradaFuncion = QLineEdit(self)  # Campo donde el usuario escribe la función f(x)
        self.entradaA = QLineEdit(self)  # Campo donde el usuario escribe el valor de a
        self.entradaB = QLineEdit(self)  # Campo donde el usuario escribe el valor de b

        # Aplicamos un estilo a los campos de entrada
        self.estilizarInput(self.entradaFuncion)
        self.estilizarInput(self.entradaA)
        self.estilizarInput(self.entradaB)

        # Agregamos los campos de entrada en la interfaz en posiciones específicas
        self.layout().addWidget(self.entradaFuncion, 2, 0, 1, 2, alignment=Qt.AlignHCenter)  # Función en fila 2, columna 0-1
        self.layout().addWidget(self.entradaA, 2, 2, 1, 1, alignment=Qt.AlignHCenter)  # "a" en fila 2, columna 2
        self.layout().addWidget(self.entradaB, 2, 3, 1, 1, alignment=Qt.AlignHCenter)  # "b" en fila 2, columna 3

         # Creamos el boton y lo agregamos en la fila 4, columna 0, ocupando 4 columnas
        self.boton = QPushButton("Calcular", self)
        self.boton.clicked.connect(self.iniciarCalculo)  # Cuando se presiona, ejecuta iniciarCalculo()
        self.boton.setFixedSize(100, 40)  # Ajustamos su tamaño
        self.boton.setStyleSheet("text-align: center; color: black; background-color: grey;")  # Estilo visual
        self.layout().addWidget(self.boton, 4, 0, 1, 4, alignment=Qt.AlignHCenter)  # Lo colocamos en fila 4 y ocupa 4 columnas

        # Ajustamos las columnas para que se distribuyan bien
        for i in range(4):
            self.layout().setColumnStretch(i, 1)

        self.hide()  # Ocultamos el frame hasta que se seleccione el método

    # Función para agregar etiquetas de texto a la interfaz
    def agregarEtiqueta(self, texto, fila, columna):
        etiqueta = QLabel(texto)  # Creamos una etiqueta con el texto dado
        etiqueta.setFont(QFont("Arial", 14))  # Le ponemos una fuente más grande
        etiqueta.setStyleSheet("color: black")  # Color del texto
        etiqueta.setFixedHeight(50)  # Altura fija para que no se vea desordenado
        etiqueta.setAlignment(Qt.AlignHCenter)  # Centramos el texto
        self.layout().addWidget(etiqueta, fila, columna, 1, 1)  # La colocamos en la fila y columna indicadas

    # Función para darle estilo a los campos de entrada
    def estilizarInput(self, campo):
        campo.setStyleSheet("text-align: center; color: black; background-color: grey;")  # Estilo visual

    # Este es el metodo que se usa al pulsar el boton
    def iniciarCalculo(self):
        funcion_str = self.entradaFuncion.text()  # Obtenemos la función ingresada
        try:
            a = float(self.entradaA.text())  # Convertimos "a" a número
            b = float(self.entradaB.text())  # Convertimos "b" a número
        except ValueError:  # Si hay un error, significa que el usuario ingresó texto en lugar de números
            print("Error: Ingresa valores numéricos para a y b.")  # Mensaje de error
            return  # Salimos de la función

        # Llamamos a la función que aplica el método de falsa posición
        self.calcularFalsaPosicion(funcion_str, a, b)

    # Implementación del método de falsa posición
    def calcularFalsaPosicion(self, funcion_str, a, b):
        try:
            f = lambda x: eval(funcion_str, {"x": x, "math": math})  # Convertimos el texto de la función en código ejecutable

            # Verificamos que f(a) y f(b) tengan signos opuestos
            if f(a) * f(b) >= 0:
                print("El intervalo no es válido, f(a) y f(b) deben tener signos opuestos.")  # Mensaje de error
                return

            iteraciones = []  # Lista para almacenar las aproximaciones de la raíz
            errores = []  # Lista para almacenar los errores en cada iteración
            erRelPorcentual = []  
            iteracion = 1  # Contador de iteraciones
            c_anterior = None  # Para almacenar la raíz anterior y calcular el ERP

            # Bucle que repite el cálculo hasta encontrar la raíz o alcanzar el límite de iteraciones
            while True:
                # Aplicamos la fórmula de falsa posición
                c = (a * f(b) - b * f(a)) / (f(b) - f(a))
                fc = f(c)  # Evaluamos la función en c

                # Si f(c) es muy pequeño, tomamos c como la raíz
                if abs(fc) < 1e-6:
                    break  # Salimos del bucle

                iteraciones.append(f"{c:.6f}")  
                errores.append(f"{abs(fc):.6f}")  

                # Cálculo del Error Relativo Porcentual (ERP)
                if c_anterior is not None:
                    erp = abs((c - c_anterior) / c) * 100
                    erRelPorcentual.append(f"{erp:.6f}")  
                else:
                    erRelPorcentual.append("N/A")  # No hay ERP en la primera iteración
                
                c_anterior = c  

                # Actualizamos el intervalo [a, b] según el signo de f(c)
                if f(a) * fc < 0:
                    b = c  # La raíz está entre a y c
                else:
                    a = c  # La raíz está entre c y b

                iteracion += 1  # Aumentamos la iteración
                if iteracion > 100:  # Si llega a 100 iteraciones, detenemos el proceso
                    print("Se alcanzó el número máximo de iteraciones.")
                    break

            # Creamos la tabla con los datos obtenidos
            data = {
                'Iteración': [str(i) for i in range(1, len(iteraciones) + 1)],
                'Aprox. Raíz': iteraciones,
                'Error': errores,
                'Error Rel. %': erRelPorcentual  
            }

            tabla = crear_tabla(data, self, 120)  # Generamos la tabla

            #tabla = Tabla(["Iteración", "Aprox. Raíz", "Error f(c)", "Error Rel. %"], self)  

            # Limpiar la tabla antes de agregar nuevos datos
            # self.tablaResultados.setRowCount(0)

            # Agregar cada fila a la tabla
            # for i in range(len(iteraciones)):
            # self.tablaResultados.add_row([
            #  i + 1,           # Número de iteración
            # iteraciones[i],  # Aproximación de la raíz
            # errores[i]       # Error absoluto
            # ])

            # Agregamos las filas con los datos
            for i in range(len(iteraciones)):
                tabla.add_row([
                    i + 1,           
                    iteraciones[i],  
                    errores[i],       
                    erRelPorcentual[i]  # Se muestra en la tabla
                ])

            tabla.setFixedHeight(300)
            tabla.setFixedWidth(600)
            self.layout().addWidget(tabla, 5, 0, 1, 4, alignment=Qt.AlignHCenter)  # Agregamos la tabla a la GUI

            # self.tablaResultados = Tabla(["Iteración", "Aprox. Raíz", "Error"], self)
            # self.layout().addWidget(self.tablaResultados, 5, 0, 1, 4, alignment=Qt.AlignHCenter)


            print(f"Raíz encontrada: {c:.6f}")  # Mostramos la raíz final en la consola

        except Exception as e:
            print(f"Error al evaluar la función: {e}")  # Si hay un error, lo mostramos