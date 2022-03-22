import sys
from builtins import super

from PyQt5.QtCore import QPropertyAnimation

from clases.Caracter import Caracter
from disenio.interfaz import *


class Alfabeto(Caracter):

    def __init__(self):
       super.__init__()

    def union(self,conjuntoA,conjuntoB):
       return conjuntoA | conjuntoB

    def intersección(self,conjuntoA,conjuntoB):
        return conjuntoA & conjuntoB






