"""
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
# x = 10
y = 2
# z = x + y print(id(x)) las LITERALES se escriben x624(Son los ultimos tres numeros del id, se los llama
# REFERENCIA), cuando se vuelve a ejecutar, cambia la literal.

# Se puede hacer una referencia del tipo de
# varialbe, de la forma siguiente, VARIABLE: (TIPO DE VARIABLE)
# los booleanos, se escriben True o False
a: str = "Hola alumnos"
# type, nos permite ver el tipo de dato que
# almacena la variable "a"
print(type(a))

# Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola mundo"
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
MiGrupoFavorito = "The Letter Black"
caracteristicas = "The Best Rock Band"
print("Mi grupo faborito es: ", MiGrupoFavorito, caracteristicas)

#numero1 = "7"
#numero2 = "8"
#print(int(numero1) + int(numero2))

# Tipos Boleanos (bool)
miBooleano = 1 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# función input
#resultado = input("Digite un numero: ")  # regresa un dato tipo string
#print(resultado)

# Conversión de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo nuemro: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
"""
"""
# Operadores Aridmeticos
operadorA = 8
operadorB = 5
suma = operadorA + operadorB
#print("Resultado de la suma: ", suma)
#interpolacion, cuando se hace de esta forma
print(f'El resultado de la suma es:{suma}')

resta = operadorA - operadorB
print(f"El resultado de la resta es:{resta}")

multiplicacion = operadorA * operadorB
print(f"El resultado de la multiplicación es: {multiplicacion}")

divicion = operadorA / operadorB
print(f"El resultado de la divición es: {divicion}")
divicion = operadorA // operadorB
#Da un numero entero.
print(f"El resultado de la divición (int) es: {divicion}")
modulo = operadorA % operadorB
print(f"El resultado de la divición o residuo (modulo) es: {modulo}")
exponente = operadorA ** operadorB
print(f"El resultado del exponente es: {exponente}")
"""
"""
# Area y perimetro de un rectángulo


altoDelRectangulo = int(input('Proporcione el largo del resctángulo'))
anchoDelRectangulo = int(input('Proporcione el ancho del resctángulo'))

area = altoDelRectangulo * anchoDelRectangulo
perimetro = (altoDelRectangulo + anchoDelRectangulo) * 2

print(f"El area del rectángulo es: {area}")
print(f"el perimetro del rectángulo es: {perimetro}")
"""
"""
miVariable3 = 10
print(miVariable3)

# Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)
# Mas resumido
miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 2
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# Operadores de Comparación
d = 4
b = 2
resultado = d == b # Comprobar si son iguales
print(resultado)

# Operadores diferentes
resultado = d != b
print(resultado)

# Operador Mayor que
resultado = d > b
print(resultado)

# Operadore Menor que
resultado = d < b
print(resultado)

# Operador Menor o igual que
resultado = d <= b
print(resultado)

#Operador Mayor o igual que
resultado = d >= b
print(resultado)
"""
"""
num = int(input('Ingresa un numero: '))
print(f'El residuo de la división es: {num % 2}')
if num % 2 == 0:
    print(f'El valor de numero es: {num} es un numero PAR')
else:
    print(f'El valor del numero es: {num} es un numero INPAR')
"""
"""
num = int(input("Ingrese un numero: "))
if num >= 18:
    print(f'Eres mayor de edad: {num}')
else:
    print(f'Eres menor de edad: {num}')
"""
"""
# Operador logico
a = False
b = False
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
"""
"""
num = int(input("Escriba un nuemro: "))
if num >= 0 and num <= 5:
    print(f"Esta dentro del rango: {num}")
else:
    print(f"Esta fuera de rango: {num}")
"""
"""
#Ejercicio or, not
vacaciones = True
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Tiene trabajo que hacer")
else:
    print("Puede asistir al juego")
"""
"""
# Ejercicio: Rango entre 20 y 30 años
edad = int(input("Que edad tienes: "))

# Forma teorica (No se usa)
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    if veinte:
        print('Esta dentro del rango de los (20\'0) años')
    elif treinta:
          print('Esta dentro del rango de los (30\'0) años')
else:
    print("No esta dentro del rango de los 20 a 30 años")
"""
"""
# Forma correcta 
if (edad >= 20 and edad < 20) or (edad >= 30 and edad < 40):
    print("Esta dentro del rango de los  (20) a (30) años" )
else:
    print("No esta dentro del rango de los 20 a 30 años")
"""
"""
# Forma Sintaxis simplificada del operador and
if (20 <= edad < 30) or (30 <= edad < 40):
    print("Esta dentro del rango de los  (20) a (30) años" )
else:
    print("No esta dentro del rango de los 20 a 30 años")
"""
"""
# Ejercicio El mayor de dos números
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2:
    print(f"El numero mayor es {num1}")
else:
    print(f"El numero mayor es {num2}")
"""

# Ejercico de Tienda de libros
print("Ingrese los datos del libro")
print("")
nombreLibro = input("Ingrese el nombre del libro")
idLibro = int(input("Ingrese el ID del libro"))
precioLibro = int(input("Ingrese el Presio del libro"))
print("El envio fue gratis, Escriba 1 (Si lo fue) y 2 (Si no lo fue)")
EnvioGratis = input("Dijite su respuesta")

print("Mostrar Respuestas")
print(nombreLibro)
print(idLibro)
print(precioLibro)
if EnvioGratis == 1:
    print("El envio fue gratis")
else:
    print("El Envio fue pagado")





