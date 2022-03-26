import sys
from builtins import super

from PyQt5.QtCore import QPropertyAnimation

from clases.Caracter import Caracter
from disenio.interfaz import *


class Alfabeto(Caracter):

    def __init__(self,conjuntoA,conjuntoB):
        self.conjuntoA = set(conjuntoA)
        self.conjuntoB = set(conjuntoB)

    def getConjuntoA(self):
        return self.conjuntoA

    def getConjuntoB(self):
        return self.conjuntoB

    def union(self):
      return self.conjuntoA.union(self.conjuntoB)

    def intersección(self):
        return self.conjuntoA.intersection(self.conjuntoB)

    def diferencia (self):
        return self.conjuntoA.difference(self.conjuntoB)

    def mostrarDatos(self, conjunto):
     text=''
     for dato in conjunto:
       text +=' '+dato

     if text=='':
         return '{ }'
     else:
         return text










