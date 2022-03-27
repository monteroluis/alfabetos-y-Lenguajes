from clases.Alfabeto import Alfabeto
from itertools import  product

class Lenguaje(Alfabeto):
 pass
 def concatenacion(self,lenguajeB):
   concatenado=list(product(self.conjunto,lenguajeB))
   return set(concatenado)

