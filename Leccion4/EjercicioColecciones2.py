#Ejercicio 2: Operaciones de conjuntos con listas
#Escribe un programa que tenga 2 listas y que a continuación
#cree las siguientes listas (en las que no deba haber repetición)
# 1 lista de palabras que aparecen en las listas
# 2 lista de palabras que aparecen en la primera lista, paro no en la segundo
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

lista1 = ['Hola', 'chau', 'casa', 'Gabriel', 4, 5, 8]
lista2 = ['auto', 'Gabriel', 'camion', 'Hola', 4, 6, 9]

#Eliminar los elementos repetidos de ambas listas con conjunto
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) #Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) #Solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) #Solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2) #Mostramos elementos que coinciden en ambas listas

print(f'lista de palabras que aparecen en las listas: {union}')
print(f'lista de palabras que aparecen en la primera lista, paro no en la segundo: {solo1}')
print(f'lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}')
print(f'lista de palabras que aparecen en ambas listas: {interseccion}')
