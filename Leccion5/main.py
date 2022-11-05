def show(name, lastName):
    print(name+' '+lastName)
persona = ['Ariel', 'Betancud']
show(persona[0], persona[1]) # Pasamos uno por uno los datos de la lista a la función
show(*persona) # Esto es lo mismo que lo anterior pero le pasamos todo junto
persona2 = ('Osvaldo', 'Giordanini') #Desempaquetamos a traves de una tupla
show(*persona2)
persona3 = {'LasName:': 'Lucero', 'name': 'Natalia'}
show(*persona3)

numbers = [1, 2, 3, 4, 5] # Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta seria la unica manera para que no se mostrara el else
else:
    print('Esto se termino')

# List comprehension, lista de comprensión
names = ['Paola', 'Rodrigo', 'Lucas', 'Pepe']
alongP = [p for p in names if p[0] == 'P']# Esto regresa una nueva lista, Va a retornar los nombres con
                                            # con la primer letra P.
print(alongP)


#bottleC = [{'name:': 'Quilmes', 'Country': 'Arg'},
           #{'name:': 'Corona', 'Country': 'Mx'},
           #{'name:': 'Stella Artois', 'Country': 'Belgica'}],

#Arg = [b for b in bottleC if b['Country'] == 'Arg']
#print(Arg)
#print(bottleC)

# Paso de Argumentos (funciones)

def mi_funcion2(name, lastName):
    print('Saludos a todos lo que ven a través del canal de YouTube')
    print(f'Nombre: {name}, apellido: {lastName}')
mi_funcion2('Jose', 'Lucas')
mi_funcion2('Ariel', 'Beta')
mi_funcion2('Ana', 'Pedro')

#La palabra return en funciones
#Creamos una función para sumar

def sumar(a, b):
    return a + b
#resultado = sumar((78, 22))
#print(f'El resultado de la suma es : {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45 )}')

def sumar2(a = 0 , b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'resultado de la suma: {resultado}')
print(f'Resultado de a suma: {sumar2(22, 66)}')

# Argumentos, varialbes en funciones
def listarNombres(*nombres): #Cuando no se tiene idea cantidad de argumentos a resibir
    for nombre in nombres:
        print(nombre)

listarNombres('Lucas', 'Jose', 'Claudio', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe')

def listaTerminos(**terminos): #Se utiliza el **, Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # kwargs sognifica: key word argument
        print(f'{llave}: {valor}')
listaTerminos() # No recibe nada, se va a mostrar
listaTerminos(IDE='Integrated Develoment Enviroment', PK='Primaruy Key')
listaTerminos(Nombre='Leonel Messi')

def desplegarNombre(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombre(nombres2)
desplegarNombre('Carlos')
# desplegarNombre(10, 11) #No es un objeto iterable
desplegarNombre(()) #Tupla
desplegarNombre([])

# Función Recursivos
def factorial(numero):
    if numero == 1: #Caso base
        return 1
    else:
        return numero * factorial(numero-1) #Caso recursivo
resultado = factorial(5) #Lo hacemos en código duro
print(f'El factorial del numero 5 es: {resultado}')# Tarea para que el usuario ingrese el factorail

