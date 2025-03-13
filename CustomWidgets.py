import sys
from PySide6.QtGui import QFont
from PySide6 import QtGui, QtCore, QtWidgets

from PySide6.QtCore import Qt


class SideBarButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        style = '''

            QPushButton{
                color: black;
                height: 25px;
                border:none;

            }
            QPushButton:hover {
                background-color: yellow;
            }
        '''
        self.setText(text)
        self.setStyleSheet(style)

class TitleLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        font = QFont("Arial", 26)
        self.setFont(font)
        style = '''
            color: black;
        '''
        self.setText(text)
        self.setStyleSheet(style)
        self.setAlignment(Qt.AlignCenter)


class TextLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        style = '''
            color: black;
            height: 25px;
        '''
        self.setText(text)
        self.setStyleSheet(style)


class Tabla(QtWidgets.QTableWidget):
    def __init__(self, columns_labels, parent=None):
        super().__init__(parent)

        self.setColumnCount(len(columns_labels))
        self.setHorizontalHeaderLabels(columns_labels)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)


    def add_row(self, row_data):
        """
        Añade una nueva fila a la tabla

        Parametros
        ----------
        row_data    : Lista de valores que va a ir en la fila, tiene que ser del mismo tamaño que la cantidad de columnas
        """

        row_pos = self.rowCount()
        self.insertRow(row_pos)
        for column, value in enumerate(row_data):
            self.setItem(row_pos,column, QtWidgets.QTableWidgetItem(str(value)))




