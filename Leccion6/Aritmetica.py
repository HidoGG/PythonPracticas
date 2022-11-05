# Creando una clase
class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentación de la clase python
    vamos a hacer en esta clase algunas operaciones de: suma, resta , multiplicación y más

    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    # Metodo para resta
    def resta(self):
        return self.operandoA - self.operandoB

    # Metodo para multiplicar
    def multiplicar(self):
        return self.operandoA * self.operandoB

    # Metodo para dividir
    def divid(self):
        return self.operandoA / self.operandoB


# Creamos el objeto de la instancia aritmetica
aritmetica1 = Aritmetica(7, 9)  # Le pasamos los argumentos para los operados A y B.
#De esta forma, solo llama a los metodos para calcular.
print(f'La suma de los numeros es: {aritmetica1.sumar()}')  # No hace falta pasar argumentos, ya lo pase arriba

print(f'la resta de los numeros es: {aritmetica1.resta()}')

print(f'la multiplicar de los numeros es: {aritmetica1.multiplicar()}')

print(f'dividir el numeros es: {aritmetica1.divid():.2f}')  # :.2f Para que muestre dos numeros flotantes
