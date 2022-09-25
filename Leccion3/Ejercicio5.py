"""
Ejercico 5: Calcular el factorial de un numero mayor o igual
a 0.
"""

num = 0

while num <= 0:
    num = int(input('Digite un numero'))

i = 1
factorial = 1

while i <= num:
    factorial *= i
    i += 1

input(f'El factorial es: {factorial}')
