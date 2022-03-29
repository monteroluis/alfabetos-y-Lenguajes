import random
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

    def Cerradura(self):
        lenguaje = list()
        while len(set(lenguaje)) != 10:
            potencia = random.randint(1, 5)  # numero de caracteres en la palabra
            palabra = ''
            for i in range(potencia):  # creacion de la cadena
                letra = random.choice(list(self.conjunto))
                palabra = letra + palabra
            lenguaje.append(palabra)
        return set(lenguaje)


    def __str__(self):
        return '{' + ','.join(self.conjunto) + '}'
