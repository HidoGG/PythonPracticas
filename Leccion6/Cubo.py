class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con un método
    calcular_volumne que tendrá la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """
    #Ingresando los atributos ancho, alto, profundidad
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    #Creamos el metodo para calcular
    def calcular_volumne(self):
        return self.ancho * self.alto * self.profundidad
#Pidiendo datos al usuario
ancho = int(input('Digite un numero para el ancho del Cubo: '))
alto = int(input('Digite un numero para el alto del Cubo: '))
profundidad = int(input('Digite un numero para la profundidad del Cubo: '))

#Instanciamos un objeto de la clase Cubo
cubo1 = Cubo(ancho, alto, profundidad)
print(f'El volumen del cubo es : {cubo1.calcular_volumne()}')