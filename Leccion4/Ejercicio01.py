#Ejercicio 1: LLenar una lista
#Llenar una lista con los números del 1 al 50, liego mostrar
#la lista con el bucle for, los elementos deben mostrar
#de la siguinte forma:
#  1-2-3-4-5....-50
"""
lista = []
for i in range(1, 51):
    lista.append(i)
    i =+ 1

print(lista)
"""
"""
lista = []
i = 1
while i <= 50:
    lista.append(i)
    i += 1
for i in lista:
    print(i,end='-')
"""

lista = list(range(1, 51))
for i in lista:
    print(i, end='-')



