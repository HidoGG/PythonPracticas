"""
#Lección 4
nombre = ['Naty', 'Osvaldo', 'Lily', 'Ariel']

print(nombre)
#Usar numero del indice
print(nombre[2])
#Usar numero negativo. Del ultimo al primero
print(nombre[-1])
"""
"""
#Recuperar
nombre = ['Naty', 'Osvaldo', 'Lily', 'Ariel']

#Solo recorre un rango del indice
#Solo mostrara el indice 0 y 1
print(nombre[0:2])

#Ir del indice de la lista al inice (Sin incluirlo)
#El compilador da como entendido que queremos del 0 al 3
#print(nombre[ :3])

#Desde el indice indicado al final
#Se ejecutara del indice 1 al ultmo
#print(nombre[1: ])

#Modificar un valor en la lista
#Se modifica el inidce 3 de la lista
#nombre[3] = 'Liliana'

#nombre[0] = 'Natalia'
#print(nombre)

#Interar una lista con ciclo For

#for nombre in nombre: #nombre es singular, la lista es plurar
    #print(nombre)
#else:
    #print('Se acabaron los elementos de la lista')

#Elementos de una lista
print(len(nombre)) #Le pasamos como parametro la lista

#Agregar un elemento
nombre.append('Marcelo')
nombre.append([1, 2, 3])#Agrega una lista, dentro de otra
nombre.append(True)#Agrego en una lista un elemento Bool
nombre.append(10.35888)#Numero tipo float
nombre.append([4, 5])#Otra lista
nombre.append(7)#Numero tipo entero
print(nombre)

#Insertar un elemento en un indice especifico
nombre.insert(1,'Alberto')
print(nombre)
nombre.insert(3,'Debora')
print(nombre)

#Eliminar un elemento
nombre.remove('Alberto')
print(nombre)

#Eliminar el ultimo elemento de la lista
nombre.pop()
print(nombre)
"""
"""
#Eliminar un indice especifico
del nombre[2] #del significa delet (Eliminar)
print(nombre)

#Eliminar, borrar o limpiar todos los elemenots
nombre.clear()
print(nombre)

#Eliminar la lista
del nombre
print(nombre) 
#Tubiera que mostrar un error de lista eliminada
#en mi caso, no paso eso.
"""
"""
#Ejercicio de practica del Dia 16/08 en Laboratorio II

print('Rango de 0 al 10 con numero divisible entre 3')
numeje1 = []
for i in range(0, 11):
    if i % 3 == 0:
        numeje1.insert(i, i)
print(numeje1)

print('Rango con valores de inicio = 2 y fin = 6')
numeje2 = []
rango = range(2, 7) #Otra forma de hacerlo
for i in rango:
    numeje2.insert(i, i)
print(numeje2)

print('Crear un rango de 3 a 10 pero en 2 en 2')
numejer3 = []
for i in range(3, 11, 2):
    numejer3.insert(i, i)
print(numejer3)
"""
"""
#Tupla la primera parte
#Son inmutables, no se pueden modificar
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
#Mostrar de manera inversa
print(cocina[-1])

#Acceder a un rango
print(cocina[0:2])

# ejemplo
verduras = ('papa') #Esto es un Str cadena, no es Tupla, falta la coma
verdura = ('papa',) #Esto es Tupla, tiene la coma

#Segunda parte de Tupla

#Recorremos los elementos de la Tupla
for cocinar in cocina:
    print(cocinar, end=" ")
    #Para que no me haga salto de linea end=" "
    #Sino print me hace un salto de linea porque tiene \n

#No es una buena practica, pero se puede modificar una tupla
#Asiendo una convercion de lista atupla y viseversa

#Ahora nuestra Tupla, pasa a ser una lista
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n',cocina) #Uso el \n para que se separe del FOR

#Eliminar cocina, aparece un erros
#del cocina

tupla = (13, 1, 8, 3, 2, 5, 8)
for i in tupla:
    if i < 5:
        print(i, end=" ")

"""
"""
#Tipo set o conjunto
#Sin orden y sin indice (Set o conjunto)

planetas = {'Marte', 'Júpiter', 'Venus'}
#Cambia el orden al ejecutar la consola
#print(planetas)

#Cantidad de elementos
#print(len(planetas))#Nos devulve 3. Por la cantidad de elementos

#Revisar si un elemento existe dentro de set,
#Pero tiene que estar igual escrito.
#print('Marte' in planetas)#Nos devulve True. Existe!!
#Tmbien se puede preguntar por si no esta
#print('Marte' not in planetas)#Nos devuelve Falso.Porque esta.

#Agregar un elemento
planetas.add('Tierra') # add es una función
print(planetas)
#No se pueden agragar elementos duplicados o repetidos
planetas.add('Tierra') #No devulve nada, siguen los mismos elementos.

#Eliminar elementos, puede arrojar un error, si el elementos no existe
#Tambien puede tirar error, si se escribe mal el elemento
planetas.remove('Júpiter')
print(planetas)
#Con discard, no te tira error si te equivocas al escribir el elemento
#Solo si ingresas mal el elemento, no se va a borrar
planetas.discard('Tierra')
print(planetas)

#Limpiar ser
planetas.clear()
print(planetas)

#Eliminar set
del planetas
print(planetas)#Nos tira Error, porque ya no existe
"""
"""
#'Maradona': 10 Un diccionario esta compuesto por dos elementos
#Una llave y un Valor
#dict(key,value)

diccionario = {
    'IDE': 'Integrated Development Evironment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de administración de Base de datos'
}
print(diccionario)
#Cantidad de elementos
print(len(diccionario))
#Acceder a un elemento de un diccionario con la llave(kay)
print(diccionario['IDE'])
#Otra forma de acceder al diccionario
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Mosidicar un elemento
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)#Me modifica. El valor en IDE

#Como recorrer los elementos
for termino in diccionario:
    print(termino)#Nos mostraria las key

#Una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)#Nos muestra tanto la Key como Valor

#Otra manera de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)#Solo se veran las llaves

for valor in diccionario.values():
    print(valor)#Nos va a mostrar solo los valores

#Comprobar la existencia de algun elemento
print('IDE' in diccionario)#Nos devulve True, esta el valor

#Agregar un elemento
diccionario['PK'] = 'Primary kay'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')#Se elimina la kay y value
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#eliminar el dicionario
del diccionario
"""
"""
#Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2 #Concatenación
print(lista3)

#Agregar varios elementos a una lista
lista3.extend([7, 8, 9])
print(lista3)

print(lista3.index(5))#Función para ubicar en que indice esta el valor ingresado

#print(lista3.index(0))#Esto dara un error por no ser el elemento parte de la lista

#Como saber cuantos valores estan repetidos en una lista
print(lista3.count(1))#Cuenta cuantos valores estan repetidos que se parescan a ese valor

#Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3]*2
print(lista3)

#Metodo ordenamiento
#Los ordena de manera acendente
lista3.sort()
print(lista3)
#Ordenarlo al rever de mayor a menor
lista3.sort(reverse=True)
print(lista3)

#Repaso de Tupla
tupla = (4, 'Hola', 6.78, [1, 2, 3], 4, 'Hola')
print(tupla)

print(4 in tupla)#Preguntar SI esta
"""
"""
#Resapo del tipo set o conjunto

#Definir un conjunto

#Con set(), se puede agregar, estando
#vacio
conjunto = set()

#No puede estar con llaves, sino no se
#puede ingresar
conjunto1 = {'bay', }

#Ingresar datos, con .add(),
# solo permite uno a la vez

conjunto.add(7)
conjunto.add('Hola')
print(conjunto)

conjunto1.add('hola')
print(conjunto1)

#pregunta si el nuemro 3
#No esta en el conjunto1
print(3 not in conjunto1)

#Como hacer la igualdad
#de dos conjuntos
print(conjunto == conjunto1)

#Operaciones en conjunto

#Union de conjuntos
conjunto3 = conjunto | conjunto1

#Se unen los conjuntos
print(conjunto3)
#No pueden ver dos elementos iguales,
#si llega a pasar, uno se borra.

#Intercepcion
#que elementos tienen en comun
conjunto3 = conjunto & conjunto1
print(conjunto3)

#Asigna el valor que esta en el conjunto y
#no en el conjunto1
conjunto3 = conjunto - conjunto1
print(conjunto3)


conjunto3 = conjunto ^ conjunto1 #No comparten y son diferentes entre ambos
print(conjunto3)


conjunto3 = conjunto | conjunto1
#Si el conjunto es un conjunto del conjunt3
print(conjunto.issubset(conjunto3))
#Tira true porque se guardan los otros

print(conjunto1.issubset(conjunto3))
#Tira true porque estan dentreo del conjunto3

print(conjunto3.issubset(conjunto1))

print(conjunto3.issuperset(conjunto))
print(conjunto3.issuperset(conjunto1))
#Tira true porque es un super conjunto
print(conjunto1.issuperset(conjunto3))
#Tira false porque no es un super conjjunto

#Como saber si ambos conjuntos son disconexos,
#esto es si no comparten elementos en comun
print(conjunto.isdisjoint(conjunto1))
#No hay cosas en comun, por eso es True

#Convertir un conjunto totalemte en inmutable
conjunto = frozenset # Esto hace que el conunto sea totalemente inmutable
#NO se pueda agregar, modificar o eliminar

#Repaso Diccionario
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

#Como eliminar, llave y valor
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'edad': 40, 'altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'altura': 1.70, 'Precio': '50 millones', 'Posición': 'Extremo derecho'},
    11: {'Nombre': 'Angel di maria', 'Edad': 34, 'altura': 1.80, 'Precio': '12 millones', 'Posición': 'Extreemo derecho'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'altura': 1.77, 'Precio': '35 millones', 'Posición': 'Media puntaa'},
    19: {'Nombre': 'Nicoás Otamendi', 'Edad': 34, 'altura': 1.83, 'Precio': '3.5 millones', 'Posición': 'Defensa central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'altura': 1.87, 'Precio': '3.5 millones', 'Posición': 'Portero'},
    27: {'Nombre': 'Julián Álvarez', 'Edad': 22, 'altura': 1.73, 'Precio': '23 millones', 'Posición': 'Delantero'},
    16: {'Nombre': 'Lisandro Martínez', 'Edad': 24, 'altura': 1.75, 'Precio': '32 millones', 'Posición': 'Defensa'},
    22: {'Nombre': 'Lautaro Martínez', 'Edad': 25, 'altura': 1.74, 'Precio': '75 millones', 'Posición': 'Delantero'},
    26: {'Nombre': 'Nahuel Molina', 'Edad': 24, 'altura': 1.75, 'Precio': '20 millones', 'Posición': 'Defensa'}
}

#Recorrer
for llave in seleccionArgentina.values():
    print(llave)


for llave, valor in seleccionArgentina.items():
    print(llave, valor)

#Como tarea agregar por lo menos 4 jugadores de
#La seleccion agrentina
print('Tenemos cargados en el diccionario la cantidad de: ', end=' ')
print(len(seleccionArgentina), 'jugadores')

# Pilas usando listas
pila = [1, 2, 3]

#Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacando elementos por el final
elementoBorrar = pila.pop() #Elimina el ultimo elemento de la sita
print(elementoBorrar) #Me guarda el elemento eliminado

#Metodos con lista llamado Cola
#Estructura de datos de tipo fifo(first input / first output) primero en entrar y primero en salir
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

#Agregar elementos al final de la lista
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacar elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
"""

