import sys
import random
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox
from clases.Alfabeto import Alfabeto
from clases.Lenguaje import Lenguaje
from disenio.interfaz import *


class Principal(QtWidgets.QWidget):

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)

        # =============customizacion===================
        self.sombra(self.ui.btnLenguajes)
        self.sombra(self.ui.btnAlfabetos)
        self.sombra(self.ui.pushButton_4)
        self.sombra(self.ui.pushButton_5)
        self.sombra(self.ui.pushButton_6)
        self.sombra(self.ui.btnAlfabetos)

        self.ui.btnMenu.clicked.connect(self.transicionLateral)
        self.ui.btnUnion.clicked.connect(lambda: self.mostrarDatos(self.ui.btnUnion.text()))
        self.ui.btninterseccion.clicked.connect(lambda: self.mostrarDatos(self.ui.btninterseccion.text()))
        self.ui.btnDiferencia.clicked.connect(lambda: self.mostrarDatos(self.ui.btnDiferencia.text()))
        self.ui.btn_cerradura.clicked.connect(lambda: self.mostrarDatos(self.ui.btn_cerradura.text()))
        self.ui.btngenerarlenguaje.clicked.connect(self.generarLenguajes)
        self.ui.btngenerarlenguaje.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.paginaLenguajes))
        self.ui.btnAlfabetos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.paginaAlfabetos))
        self.ui.btnLenguajes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.paginaLenguajes))
        self.ui.btnLenUnion.clicked.connect(lambda: self.mostrarDatosLenguaje(self.ui.btnLenUnion.text()))
        self.ui.btnLenDiferencia.clicked.connect(lambda: self.mostrarDatosLenguaje(self.ui.btnLenDiferencia.text()))
        self.ui.btnLenInterseccion.clicked.connect(lambda: self.mostrarDatosLenguaje(self.ui.btnLenInterseccion.text()))
        self.ui.btnLenConcatenacion.clicked.connect(lambda: self.mostrarDatosLenguaje(self.ui.btnLenConcatenacion.text()))
        self.ui.btnLenPotencia.clicked.connect(lambda: self.mostrarDatosLenguaje(self.ui.btnLenPotencia.text()))
        self.ui.btnLenInvertir.clicked.connect(lambda: self.mostrarDatosLenguaje(self.ui.btnLenInvertir.text()))
        self.ui.btnLenCardinalidad.clicked.connect(lambda: self.mostrarDatosLenguaje(self.ui.btnLenCardinalidad.text()))

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

    def sombra(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(30)
        sombra.setXOffset(6)
        sombra.setYOffset(6)
        sombra.setColor(QColor(245, 121, 0))
        frame.setGraphicsEffect(sombra)

    def mostrarDatos(self, namebtn):
        if self.ui.lineEditConjuntoB.text() != '' and self.ui.lineEditConjuntoB.text()!='':
            alfabetoA = Alfabeto(self.ui.lineEditConjuntoA.text().split())
            alfabetoB = Alfabeto(self.ui.lineEditConjuntoB.text().split())
            if namebtn == 'Unión':
                dato = alfabetoA.union(alfabetoB)
            elif namebtn == 'Intersección':
                dato = alfabetoA.intersección(alfabetoB)
            elif namebtn == 'Diferencia':
                dato = alfabetoA.diferencia(alfabetoB)
            elif namebtn == 'Cerradura':
                dato = alfabetoA.Cerradura(4)
            self.ui.plainTextResultados.setPlainText(str(dato))
        else:
            self.messagedialog("Rellene los campos para continuar")

    def mostrarDatosLenguaje(self, namebtn):

      if self.ui.lineEditLenguajeA.text()!='' and self.ui.lineEditLenguajeB.text()!='':
        lenguajeA = Lenguaje(self.ui.lineEditLenguajeA.text().split())
        lenguajeB = Lenguaje(self.ui.lineEditLenguajeB.text().split())
        if namebtn == 'Unión':
            dato = lenguajeA.union(lenguajeB)
        elif namebtn == 'Intersección':
            dato = lenguajeA.intersección(lenguajeB)
        elif namebtn == 'Diferencia':
            dato = lenguajeA.diferencia(lenguajeB)
        elif namebtn == 'Concatenación':
            dato = lenguajeA.concatenacion(lenguajeB)
        elif namebtn == 'Potencia':
            dato = lenguajeA.potencia(3)
        elif namebtn == 'Invertir':
            dato = lenguajeA.inversa()
        elif namebtn == 'Cardinalidad':
            dato = lenguajeA.cardinalidad()
        self.ui.plainTexResultadosLen.setPlainText(str(dato))
      else:
          self.messagedialog("Genera los lenguajes en la sección alfabeto para continuar")

    def generarLenguajes(self):
        if self.ui.lineEditConjuntoB.text() != '' and self.ui.lineEditConjuntoB.text() != '':
            self.messagedialog("ganando como siempre")
            alfabetoA = Alfabeto(self.ui.lineEditConjuntoA.text().split())
            lenguajeA = alfabetoA.Cerradura(5)
            lenguajeB = alfabetoA.Cerradura(5)
            cadena = str(lenguajeA).strip("{}").replace(",", " ")
            cadena2 = str(lenguajeB).strip("{}").replace(",", " ")
            self.ui.lineEditLenguajeA.setText(cadena)
            self.ui.lineEditLenguajeB.setText(cadena2)
        else:
            self.messagedialog("Rellene los campos para continuar")


    def messagedialog(self,texto):
        message=QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText(texto)
        message.setWindowTitle("Información")
        message.setStandardButtons(QMessageBox.Ok)
       # message.buttonClicked.connect(msgButtonClick)
        returnValue = message.exec()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Principal()
    GUI.show()
    sys.exit(app.exec_())
