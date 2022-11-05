class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular_ariea  utilizando la formula:
    area = base * altura. pero la base y la altura deben ser ingresados por
    el usuario y los objetos deben ser tres.
    """
    #Atributos (Altura y base)
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
    #Metodos para calcular
    def calcular_aria(self):
        return self.altura * self.base

base = int(input('Digite un numero para la base del rectangulo: '))
altura = int(input('Digite un digito para la altura del rectangulo: '))

#Instanciamos un objeto de la clase rectangulo
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcular_aria()}')