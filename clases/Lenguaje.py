import random
from clases.Alfabeto import Alfabeto


class Lenguaje(Alfabeto):

    def cardinalidad(self):
        return len(self.conjunto)

    def concatenacion(self, conjuntoB):
        listaConcat =['⌀']
        for i in list(self.conjunto):
            palabra = (i)
            for j in list(conjuntoB.getConjunto()):
                palabraConcat = palabra + (j)
                listaConcat.append(palabraConcat)
        return Lenguaje(listaConcat)

    def potencia(self, potencia):
        listaPow=[""]
        if potencia != 0:
            for i in range(potencia):
                for j in list(listaPow):
                    palabra1 = (j)
                    for k in list(self.conjunto):
                        palabraConcat = palabra1 + (k)
                        listaPow.append(palabraConcat)
        listaPow[:0] = '⌀'
        listaPow = list(set(listaPow))
        listaPow.sort(key=len)
        del listaPow[0]
        return Lenguaje(listaPow)

    def inversa(self):
        listaInv = list()

        for i in list(self.conjunto):
            palabraInv = ((i)[::-1])
            listaInv.append(palabraInv)
        return Lenguaje(listaInv)
