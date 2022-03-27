import random
from clases.Alfabeto import *
from Principal import *
from clases.Lenguaje import Lenguaje

conjuntoA=input("digite conjunto A")
conjuntoB=input("digite conjunto B")
papa=Lenguaje(conjuntoA.split())
mama=Lenguaje(conjuntoB.split())
print(papa.concatenacion(mama.getConjunto()))