
from abc import ABC, abstractmethod

#Comvertir en una clase abstracta y un decorador
#ABC significa: abstrac Base Class, convierte una clase en abstracta

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'valor error ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'valor error ancho: {alto}')

    #Para que sea obligatorio tener el metodo
    #calcular_area en los hijos
    @abstractmethod
    def calcular_area(self):
        #Se utliza pass para que no afecte al padre
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    def _validar_valores(self, valor): # Metodo encapsular
        return True if 0 < valor < 10 else False

