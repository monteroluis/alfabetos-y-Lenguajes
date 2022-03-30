import random
class Alfabeto():

    def __init__(self, conjunto):
        self.conjunto = set(conjunto)

    def getConjunto(self):
        return set(self.conjunto)

    def setConjunto(self):
        return self.conjunto

    def union(self, conjuntoB):
        return Alfabeto(self.conjunto.union(conjuntoB.getConjunto()))

    def intersección(self, conjuntoB):
        return Alfabeto(self.conjunto.intersection(conjuntoB.getConjunto()))

    def diferencia(self, conjuntoB):
        return Alfabeto(self.conjunto.difference(conjuntoB.getConjunto()))

    def Cerradura(self,numPalabras):
        lenguaje = list()
        while len(set(lenguaje)) != numPalabras:
            potencia = random.randint(1, 5)  # numero de caracteres en la palabra
            palabra = ''
            for i in range(potencia):  # creacion de la cadena
                letra = random.choice(list(self.conjunto))
                palabra = letra + palabra
            lenguaje.append(palabra)
        return Alfabeto(lenguaje)

    def __str__(self):
        return '{' + ','.join(self.conjunto) + '}'
