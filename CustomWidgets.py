import sys
from PySide6.QtGui import QFont
from PySide6 import QtGui, QtCore, QtWidgets

from PySide6.QtCore import Qt


class SideBarButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        style = '''

            QPushButton{
                color: #ffffff;
                height: 25px;
                border:none;

            }
            QPushButton:hover {
                background-color: #607cff;
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
            color: #ffffff;
        '''

        self.setWordWrap(True)
        self.setText(text)
        self.setStyleSheet(style)
        self.setAlignment(Qt.AlignCenter)


class InputField(QtWidgets.QLineEdit):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        style = '''
            background-color: #525251;
            color: #ffffff;
            border-width: 1px;
            border-radius: 3px;
            border-color: #051a39;
            padding: 2px;
        '''
        self.setStyleSheet(style)


class Button(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        style = '''
            QPushButton{
                background-color: #607cff;
                color: #ffffff;
                border-style: solid;
                border-width: 1px;
                border-radius: 3px;
                border-color: #051a39;
                padding: 5px;
            }

            QPushButton:hover {
                background-color: #8399ff;
                color: #ffffff;
                border-style: solid;
                border-width: 1px;
                border-radius: 3px;
                border-color: #051a39;
                padding: 5px;

            }
        '''
        self.setText(text)
        self.setStyleSheet(style)


class TextLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        style = '''
            color: #ffffff;
            height: 25px;
        '''
        self.setText(text)
        self.setStyleSheet(style)


class Tabla(QtWidgets.QTableWidget):
    def __init__(self, columns_labels, parent=None):
        super().__init__(parent)
        style = '''
            background-color: #242526;
            border: 1px solid #32414B;
            color: #f0f0f0;
            gridline-color: #8faaff;
            outline : 0;
        '''

        self.setStyleSheet(style)
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




