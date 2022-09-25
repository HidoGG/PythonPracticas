#Ejercicio 6: Tabla de multiplicar
#Hacer un programa que pida un número por teclado y guarde
#en una lista su tabla de multiplicar hacer el 10. Por ejemplo:
#Si digita el 5 la lista tendra: 5, 10, 15, 20, 25 ... 50.

"""
numero = int(input('Que tabla de multiplicar quiere ver (Digite un número): '))
num = 0
for i in range(11):
    num = numero * i
    print(f'{numero} x {i} = {num}')
"""

numero = int(input('Que tabla de multiplicar quiere ver (Digite un número): '))
lista = []
for i in range(1,11):
    lista.append(i*numero)

print(f'\n Tabla de multiplicar del {numero}: \n{lista}')


for indice, i in enumerate(lista):
    #Este ciclo es para ver el formato de una tabla de multiplicar
    print(f'{numero} x {i} = {lista[indice]}')









