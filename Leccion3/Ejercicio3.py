"""
Ejercicio 3
leer 10 numeros e imprimir cuantos son pasitivos, cuantos negativos y
cuantos neutros.
"""
positivo = 0
negativo = 0
neutro = 0

for i in range(10):
    num = int(input('Ingrese un numero'))
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    else:
        neutro += 1
input(f'El resultado es: positivos son {positivo}, negativos son {negativo} y neutros son {neutro}')

