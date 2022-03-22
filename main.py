import sys
from PyQt5.QtCore import QPropertyAnimation
from disenio.interfaz import *


class Aplicacion(QtWidgets.QWidget):

    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui=Ui_Principal()
        self.ui.setupUi(self)
        self.ui.btnMenu.clicked.connect(self.transicionLateral)

    def transicionLateral(self):
        if True:
         width = self.ui.frameLateral.width()
         normal = 0

        if width == 0:
         extender = 250
        else:
         extender = normal
        self.animacion = QPropertyAnimation(self.ui.frameLateral, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()


if __name__ =='__main__':
    app=QtWidgets.QApplication(sys.argv)
    GUI=Aplicacion()
    GUI.show()
    sys.exit(app.exec_())




