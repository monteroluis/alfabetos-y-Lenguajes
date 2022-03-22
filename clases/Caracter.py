from abc import ABC,abstractmethod


class Caracter(ABC):

    @abstractmethod
    def __init__(self,conjuntoA,conjuntoB):
     self.conjuntoA=conjuntoA
     self.conjuntoB=conjuntoB

     def set_conjuntoA(self, conjuntoA):
         self.conjuntoA = conjuntoA

     def set_conjuntoB(self, conjuntoB):
         self.conjuntoB = conjuntoB

     def get_conjuntoA(self):
         return self.conjuntoA

     def get_conjuntoB(self):
         return self.conjuntoB


    @abstractmethod
    def union(self,conjuntoA,conjuntoB):
        pass

    @abstractmethod
    def intersección(self,conjuntoA,conjuntoB):
        pass

    @abstractmethod
    def diferencia(self, conjuntoA, conjuntoB):
        pass

