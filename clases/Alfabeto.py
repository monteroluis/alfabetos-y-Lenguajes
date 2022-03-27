from typing import overload


class Alfabeto():

    def __init__(self, conjunto):
        self.conjunto = set(conjunto)

    def getConjunto(self):
        return set(self.conjunto)

    def setConjunto(self):
        return self.conjunto

    def union(self, conjuntoB):
        return Alfabeto(self.conjunto.union(conjuntoB))

    def intersección(self, conjuntoB):
        return Alfabeto(self.conjunto.intersection(conjuntoB))

    def diferencia(self, conjuntoB):
        return Alfabeto(self.conjunto.difference(conjuntoB))

    def __str__(self):
        return '{' + ','.join(self.conjunto) + '}'
