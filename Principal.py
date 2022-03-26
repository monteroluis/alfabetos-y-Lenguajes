import sys
from PyQt5.QtCore import QPropertyAnimation

from clases.Alfabeto import Alfabeto
from disenio.interfaz import *

class Principal(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)
        self.ui.btnMenu.clicked.connect(self.transicionLateral)
        self.ui.btnUnion.clicked.connect(self.mostrarDatos)
        self.ui.btninterseccion.clicked.connect(self.resinterseccion)
        self.ui.btnDiferencia.clicked.connect(self.resdiferencia)
        self.ui.btnAlfabetos.clicked.connect(lambda :self.ui.stackedWidget.setCurrentWidget(self.ui.paginaAlfabetos))
        self.ui.btnLenguajes.clicked.connect(lambda :self.ui.stackedWidget.setCurrentWidget(self.ui.paginaLenguajes))
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

    def mostrarDatos(self):
        alfabeto=Alfabeto(self.ui.lineEditConjuntoA.text().split(),self.ui.lineEditConjuntoB.text().split())
        self.ui.plainTextResultados.setPlainText(alfabeto.mostrarDatos(alfabeto.union()))

    def resinterseccion(self):
        alfabeto = Alfabeto(self.ui.lineEditConjuntoA.text().split(), self.ui.lineEditConjuntoB.text().split())
        self.ui.plainTextResultados.setPlainText(alfabeto.mostrarDatos(alfabeto.intersección()))

    def resdiferencia(self):
        alfabeto = Alfabeto(self.ui.lineEditConjuntoA.text().split(), self.ui.lineEditConjuntoB.text().split())
        self.ui.plainTextResultados.setPlainText(alfabeto.mostrarDatos(alfabeto.diferencia()))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Principal()
    GUI.show()
    sys.exit(app.exec_())
