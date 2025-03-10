from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView

# Recordatorio, recomiendo no leer esto hasta que lo diga en el otro, basicamente aqui solamente esta la creacion de la tabla, lo puse aqui porque siento que queda mas bonito
# Aparte la idea es que si quieren utilizar la tabla solamente tienes que importar esta clase como lo hice al principio de la clase de mi metodo, explicare que pautas se ocupan para poder integrarlo


def crear_tabla(data, parent, ancho): # Este es el metodo que usamos en la clase donde hacemos nuestro frame para el metodo
  # data: Es el diccionario que hicimos en nuestra clase de metodo
  # parent: Ps es el self del frame de nuestro metodo
  # ancho: Este si es importante, debido a que el tamaño tiene que ps quedar bonito, hay que asignar un ancho para cada una de las columnas en nuestro metodo
  # esta anchura esta puesta para que todas las columnas sean del mismo tamaño, si quieres que todas sean del mismo ancho asegurate que el total sea menor a aproximadamente 558
  # porque 560 si se supone que el ancho de la tabla (como lo defini en la linea...) es de 600px? Ps resulta que cuando se genera una tabla vacia no se hace ninguna fila, por lo que hay mas espacio, pero despues cuando se agregan las filas se pone un numerito automaticamente al lado, es util porque asi no tenemos que indicar en cual iteracion estamos, pero de todas formas eso son como 20px
  # tambien puedes asignar el ancho de columna en base a cuantas tengas (lo explico mas adelante), si te pasas de aproximadamente 560 (no se el numero exacto) en total va a salir la barrita de desplazamiento abajo, pruebalo si quieres o si te gusta, en mi caso no

  # Ahora si, fuera del parloteo, comenzemos haciendo una tabla a partir de data
  table = QTableWidget(parent) # Asegurate de poner el parent aqui
  table.setRowCount(len(next(iter(data.values())))) #Aqui se hacen el numero de filas en base a la longitud de las listas de los valores, si hay 10 valores en los arreglos del diccionario, van a ser 10 filas
  table.setColumnCount(len(data)) # Numero de columnas segun el numero de claves (el termino correcto es claves pero yo les digo arreglos) en el diccionario

  # Rellenar la tabla con los datos, no se como chingados hicieron esto, ni me moleste en entender pero para mas informacion ir al siguiente link, lo saque de aqui https://github.com/snazrul1/PyRevolution/blob/master/PyQt4/Tables.ipynb
  horHeaders = []
  for n, key in enumerate(sorted(data.keys())):
    horHeaders.append(key)
    for m, item in enumerate(data[key]):
      newitem = QTableWidgetItem(item)
      table.setItem(m, n, newitem)

  # Establecemos los encabezados de la tabla
  table.setHorizontalHeaderLabels(horHeaders)

  # Aqui es donde esta lo del tamaño, este es el metodo que uso yo porque quiero que todas las columnas sean del mismo tamaño
  # Ajustar el tamaño de las columnas y filas
  num_columnas = table.columnCount()  # Sacamos el número de columnas de la tabla
  for i in range(num_columnas):
      table.setColumnWidth(i, ancho)
    
  # Establece el mismo ancho para todas las filas
  table.resizeRowsToContents()

  """ Ahora, si quieres hacerlo con tamaños variables, ignora lo del ancho, puedes poner el valor que quieras y da igual
  Como vamos a hacer tablas de distintos tamaños entonces tienes que poner este metodo dentro de tu propia clase del metodo que te toco,
  osea, copiar y pegar todo esto (No copies los comentarios porque si son un chingo alv), eliminas la parte donde asigno yo que todas las columnas sean del mismo tamaño
  y en su lugar pones algo como por ejemplo, en mi caso, si quisiera que mi tabla tenga una columna de 100, otra de 50 y otra de 150 seria algo asi:
  
  table.table.setColumnWidth(0, 100)
  table.table.setColumnWidth(0, 50)
  table.table.setColumnWidth(0, 150)

  y dejas lo demas como está, ahora que me doy cuenta podria hacer que se pueda agregar un arreglo donde se puedan indicar todos los anchos de tabla que desees
  pero me da hueva hacerlo tonces asi ta la cosa
  """
  # Hacemos que las tablas no sean editables despues que se crean
  table.setEditTriggers(QAbstractItemView.NoEditTriggers)

  # Termina la creacion de la tabla y se aplica el metodo
  return table