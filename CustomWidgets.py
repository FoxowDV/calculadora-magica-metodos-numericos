import sys
from PySide6 import QtGui, QtCore, QtWidgets



class SideBarButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        style = '''
            color: black;
            height: 25px;
        '''
        self.setText(text)
        self.setStyleSheet(style)






