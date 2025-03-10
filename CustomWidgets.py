import sys
from PySide6.QtGui import QFont
from PySide6 import QtGui, QtCore, QtWidgets

from PySide6.QtCore import Qt


class SideBarButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        style = '''
            color: black;
            height: 25px;
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



