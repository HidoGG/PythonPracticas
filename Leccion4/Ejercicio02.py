#Ejercicio 2: Modificar los elementos de una lista
#Llenar una lista con los numeros del 1 al 10. Luego modificar los
#Elementos de la lista multiplicandolos por un valor ingresado por el usuario

"""
numero = int(input('Ingrese un valor: '))
lista = []
for i in range(1, 10):
    lista.append(i*numero)
    i =+ 1

print(lista)
"""

lista = list(range(1, 11))
print('lista original')
for i in lista:
    print(i, end='-')
valor = int(input('\ndigite un valor a multiplicar: '))
#Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f'lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end='-')