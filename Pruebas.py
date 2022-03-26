from clases.Alfabeto import Alfabeto
from disenio.interfaz import *
from Principal import *

conjuntoA=input("digite conjunto A")
conjuntoB=input("digite conjunto B")
papa=Alfabeto(conjuntoA.split(),conjuntoB.split())

print(papa.mostrarDatos(papa.union()))

alfabeto = Alfabeto(ui.lineEditConjuntoA.text().split(), ui.lineEditConjuntoB.text().split())
ui.plainTextResultados.setPlainText(alfabeto.mostrarDatos(alfabeto.union()))






