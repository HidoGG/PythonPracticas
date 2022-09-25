#Ejercico 1: Eliminar duplicads de una lista
#Escribir un programa donde tenga una lista y que a continuación
#elimine los elementos repetidos, por ultimo mostrar la lista

#Creamos una lista
lista1 = [1, 2, 3, 3]

#Me elimina los datos repetidos set()
#conjunto = set(lista1)# Convierte la lista a un conjunto de tipo set

#lista2 = list(conjunto)#Convierte el conjunto en lista

#En una sola linea hacemos lo mismo que arriba (Codigo eficiente)
lista2 = list(set(lista1))
print(lista2)



