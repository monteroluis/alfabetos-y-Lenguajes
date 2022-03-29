import sys
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from clases.Alfabeto import Alfabeto
from disenio.interfaz import *


class Principal(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)

        self.sombra(self.ui.btnLenguajes)
        self.sombra(self.ui.btnAlfabetos)
        self.sombra(self.ui.pushButton_4)
        self.sombra(self.ui.pushButton_5)
        self.sombra(self.ui.pushButton_6)
        self.sombra(self.ui.btnAlfabetos)
        self.ui.btnMenu.clicked.connect(self.transicionLateral)
        self.ui.btnUnion.clicked.connect(self.mostrarDatos)
        self.ui.btninterseccion.clicked.connect(self.resinterseccion)
        self.ui.btnDiferencia.clicked.connect(self.resdiferencia)
        #self.ui.btnCerradura.clicked.connect(self.)
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

    def sombra(self,frame):
        sombra=QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(6)
        sombra.setYOffset(6)
        sombra.setColor(QColor(245, 121, 0))
        frame.setGraphicsEffect(sombra)

    def mostrarDatos(self):

        alfabeto1=Alfabeto(self.ui.lineEditConjuntoA.text().split())
        alfabeto2 = Alfabeto(self.ui.lineEditConjuntoB.text().split())
        self.ui.plainTextResultados.setPlainText(str(alfabeto1.union(alfabeto2.getConjunto())))

    def resinterseccion(self):
        alfabeto1 = Alfabeto(self.ui.lineEditConjuntoA.text().split())
        alfabeto2 = Alfabeto(self.ui.lineEditConjuntoB.text().split())
        self.ui.plainTextResultados.setPlainText(str(alfabeto1.intersección(alfabeto2.getConjunto())))

    def resdiferencia(self):
        alfabeto1 = Alfabeto(self.ui.lineEditConjuntoA.text().split())
        alfabeto2 = Alfabeto(self.ui.lineEditConjuntoB.text().split())
        self.ui.plainTextResultados.setPlainText(str(alfabeto1.diferencia(alfabeto2.getConjunto())))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Principal()
    GUI.show()
    sys.exit(app.exec_())
