"""
Ejercico 6: Ingresa "N" enteros, visualizar la suma de los números
pares de la lista, cuantos números pares existen y cual es el promedio
de los numeros
"""

n_elementos = int(input('Digite la cantidad de elementos a ingresar: '))

i = 1
sumaPares = 0
conteoPares = 0
sumaImpares = 0
conteoImpares = 0
while i <= n_elementos:
    i += 1
    num = int(input(f'{i-1} Digite un numero: '))
    if num % 2 == 0:
        sumaPares += num
        conteoPares += 1
    else:
        sumaImpares += num
        conteoImpares += 1


if conteoPares <= 0:
    input('No se han digitado numeros pares')
else:
    input(f'La suma de los números pares es: {sumaPares}')
    input(f'El conteo de los números pares es: {conteoPares}')

if conteoImpares <= 0:
    input('No se han digitado numeros Impares')
else:
    input(f'La suma de los números impares es: {sumaImpares}')
    input(f'El conteo de los números impares es: {conteoImpares}')

