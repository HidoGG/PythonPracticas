#Ejercicio 3: Agregar personajes a una lista
#Escribir un programa donde cree una lista con las siguientes personajes del señor de los anillos

#Nombre: Aragon
#Clase: Guerrero
#Raza: Duende del norte

#Nombre: Gandalf
#Clase: Mago
#Raza: Istar

#Nombre: Legolas
#Clase: Arquero
#Raza: Elfo Sindar

"""
listaPjSeñorDeLosAnillos = [
    {'Nombre':  'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del norte'},
    {'Nombre':  'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'},
    {'Nombre':  'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'},
    {'Nombre':  'Éowyn', 'Clase': 'Guerrero', 'Raza': 'Humano'},
    {'Nombre':  'Pippin', 'Clase': 'Guerrero', 'Raza': 'hobbit'},
    {'Nombre':  'Merry', 'Clase': 'Guerrero', 'Raza': 'hobbit'}]

for i in listaPjSeñorDeLosAnillos:
    print(i)
"""
listaPjSeñorDeLosAnillos = []

P = {'Nombre':  'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del norte'}
listaPjSeñorDeLosAnillos.append(P)
P = {'Nombre':  'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
listaPjSeñorDeLosAnillos.append(P)
P = {'Nombre':  'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
listaPjSeñorDeLosAnillos.append(P)
for i in listaPjSeñorDeLosAnillos:
    print(i)

