from CustomWidgets import TitleLabel, Tabla, TextLabel
import math
from PySide6.QtWidgets import QFrame, QGridLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
# -x**2+2.8*x+2.5 fokin cosa

class MetodoFalsaPosicion(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QGridLayout()) # Ponemos el layout como un grid (rejilla)
        
        # Centramos los elementos en el layout
        self.layout().setAlignment(Qt.AlignCenter)
        
        # Titulo
        titulo = TitleLabel("Método de Falsa Posición")
        self.layout().addWidget(titulo, 0, 0, 1, 4) # Añadimos el título en la fila 0, columna 0, ocupando 1 fila y 4 columnas
        
        # Texto o eiquetas para los campos de entrada - Pa que sean visibles
        labelFuncion = TextLabel("Función f(x)") 
        labelA = TextLabel("Valor de a") 
        labelB = TextLabel("Valor de b") 
        
        # Añadimos las etiquetas al layout en la fila 1
        self.layout().addWidget(labelFuncion, 1, 0, 1, 2)
        self.layout().addWidget(labelA, 1, 2)
        self.layout().addWidget(labelB, 1, 3)
        
        # Creamos campos de entrada para que el usuario ingrese datos
        self.entradaFuncion = QLineEdit(self)
        self.entradaA = QLineEdit(self)
        self.entradaB = QLineEdit(self)
        
        # Aplicamos estilo para texto negro de las letras
        estilo = '''
            QLineEdit {
                background-color: #f0f0f0;
                color: black;
                padding: 5px;
                border: 1px solid;
            }
        '''
        # Aplicamos el estilo a cada campo de entrada
        self.entradaFuncion.setStyleSheet(estilo)
        self.entradaA.setStyleSheet(estilo)
        self.entradaB.setStyleSheet(estilo)
        
        # Añadimos los campos de entrada al layout en la fila 2
        self.layout().addWidget(self.entradaFuncion, 2, 0, 1, 2)
        self.layout().addWidget(self.entradaA, 2, 2)
        self.layout().addWidget(self.entradaB, 2, 3)
        
        # Creamos un botón para iniciar el cálculo
        self.botonCalcular = QPushButton("Calcular", self)
        self.botonCalcular.clicked.connect(self.iniciarCalculo)
        self.botonCalcular.setFixedSize(100, 40) # Tamaño del botón a 100x40 píxeles
        # Y el estilo para el botón{
        self.botonCalcular.setStyleSheet(''' 
                background-color: #bc42a8;
                color: white;
                border: none;
                padding: 5px;
                font-weight: bold;
        ''') # Añadimos el botón en la fila 3, centrado horizontalmente
        self.layout().addWidget(self.botonCalcular, 3, 0, 1, 4, alignment=Qt.AlignHCenter)
        
        # Creamos una etiqueta para mostrar el resultado final
        self.etiquetaResultado = QLabel("El resultado va a aparecer aquí muajaja", self)
        self.etiquetaResultado.setStyleSheet("color: black; font-weight: bold;")
        self.etiquetaResultado.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.etiquetaResultado, 4, 0, 1, 4)
        
        # Tabla para mostrar los resultados
        self.tablaResultados = Tabla(["Aproximación", "Error f(c)", "Error Rel. %"])
        self.tablaResultados.setStyleSheet("color: black;") 
        self.layout().addWidget(self.tablaResultados, 5, 0, 1, 4)
        
        # Ajustamos el tamaño de las columnas para que se distribuyan bien
        for i in range(4): # Iteramos por las 4 columnas
            self.layout().setColumnStretch(i, 1) 
        
        # Ocultamos el frame primero
        self.hide()
    
    def iniciarCalculo(self):
        '''
        Método que se ejecuta cuando se presiona el botón Calcular.
        Obtiene los valores ingresados y llama al método que realiza los cálculos.
        '''
        # Limpiar la tabla para nuevos cálculos
        self.tablaResultados.setRowCount(0)
        
        # Obtener valores ingresados
        funcion_str = self.entradaFuncion.text()
        
        try: # Bloque try para capturar posibles errores
            # Convertir los valores de texto a números
            a = float(self.entradaA.text())
            b = float(self.entradaB.text())
            
            # Llamar al método de falsa posición
            raiz = self.calcularFalsaPosicion(funcion_str, a, b)
            
            # Actualizamos el  resultado
            if raiz is not None: # Pues si se encontró una raíz
                self.etiquetaResultado.setText(f"Raíz encontrada: {raiz:.4f}") # Mostramos la raíz con 6 decimales que mencionó el profe
            else: # Y si no se encontró una raíz
                self.etiquetaResultado.setText("No se pudo encontrar una raíz. Verifica tus valores.")
            
        except ValueError: # Y si hay un error al convertir los valores a flotante
            self.etiquetaResultado.setText("Error: Ingresa valores numéricos válidos para a y b.")
        except Exception as e: # U otro tipo de error
            self.etiquetaResultado.setText(f"Error: {str(e)}")
    
    def calcularFalsaPosicion(self, funcion_str, a, b): # Y este ya es el método de implementación del método de falsa posición 
        try:
            # Convertir la cadena de la función en una función que podamos evaluar
            f = lambda x: eval(funcion_str, {"x": x, "math": math})
            
            # Verificar que f(a) y f(b) tengan signos opuestos
            fa = f(a)
            fb = f(b)
            
            # Verificamos si f(a) y f(b) tienen signos opuestos multiplicándolos
            if fa * fb >= 0: # Si el producto es positivo o cero, no tienen signos opuestos
                print("Error: f(a) y f(b) deben tener signos opuestos.")
                self.etiquetaResultado.setText("Error: f(a) y f(b) deben tener signos opuestos.")
                return None # Retornamos None para indicar que no se pudo encontrar una raíz
            
            # Inicializar variables
            iteracion = 1
            c_anterior = None
            max_iteraciones = 100
            tolerancia = 0.001
            
            # Iterar hasta encontrar la raíz o alcanzar el máximo de iteraciones
            while iteracion <= max_iteraciones:
                # Calcular c usando la fórmula de falsa posición
                c = (a * fb - b * fa) / (fb - fa)
                fc = f(c)
                
                # Calcular el error absoluto
                error_abs = abs(fc)
                
                # Calcular el error relativo porcentual si tenemos un valor anterior
                if c_anterior is not None: # Si ya tenemos un valor anterior de c
                    error_rel = abs((c - c_anterior) / c) * 100
                    error_rel_str = f"{error_rel:.4f}%"
                else:
                    error_rel_str = "N/A" # No aplica para la primera iteración
                
                # Añadir la fila a la tabla
                self.tablaResultados.add_row([
                    f"{c:.4f}", # Aproximación de la raíz con 4 decimales
                    f"{error_abs:.4f}",  # Error absoluto
                    error_rel_str # Y el error relativo porcentual
                ])
                
                # Verificar si se encontró la raíz
                if error_abs < tolerancia:  # Si el error es menor que la tolerancia
                    print(f"Raíz encontrada: {c:.4f} en {iteracion} iteraciones.")
                    return c # Retornamos el valor encontrado
                
                # Actualizar intervalo
                if fa * fc < 0: # Si f(a) y f(c) tienen signos opuestos
                    b = c # Actualizamos b con el valor de c
                    fb = fc  # Actualizamos f(b) con f(c)
                else: # Si f(c) y f(b) tienen signos opuestos
                    a = c # Actualizamos a con el valor de c
                    fa = fc # Actualizamos f(a) con f(c)
                
                # Guardar el valor actual de c para calcular el error relativo en la próxima iteración
                c_anterior = c
                
                # Incrementar el contador de iteraciones
                iteracion += 1
                
            # Si se alcanzó el máximo de iteraciones
            print(f"Se alcanzó el número máximo de iteraciones ({max_iteraciones}) sin convergencia.")
            self.etiquetaResultado.setText(f"Aviso: Máximo de iteraciones alcanzado. Última aproximación: {c:.4f}")
            return c  # Retornamos la última aproximación obtenida
                
        except Exception as e:  # O cualquier error que ocurra
            print(f"Error al evaluar la función: {e}")
            self.etiquetaResultado.setText(f"Error al evaluar la función: {str(e)}")
            return None  # Retornamos No se pudo encontrar una raíz