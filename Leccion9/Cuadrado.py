# Clase hija que va a heredar de diferentes padres, es importante
# el orden de los padres.


from FiguraGeometrica import FiguraGeometrica  # Modulo y clase
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super.__init__(lado) #No lo usamos porque tenemos mas de un padre
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    # Creamos un metodo que calcula el area
    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
