"""
income = float(input("Introduce el ingreso anual:"))

#
# Escribe tu código aquí.
#

if income < 85528:
    tax = (income * 0.18) - 556.2
else:
    tax = ((income - 85528) * 0.32) + 14839.2

if tax < 0: tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

"""
"""
year = int(input("Introduce un año:"))

#
# Escribe tu código aquí.
#
if year < 1582:
    print('No dentro del período del calendario Gregoriano')
elif year % 4 != 0:
    print('Año comun')
elif year % 100 != 0:
    print('Año bisiesto')
elif year % 400 != 0:
    print('Año comun')
else:
    print('Año bisiesto')
"""
"""
secret_number = 777

print(
"""
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
"""
""")
pedirNum = int(input('Escriba un numero: '))

while pedirNum != secret_number:
    print('¡Ja, ja! ¡Estás atrapado en mi bucle!')
    pedirNum = int(input('Escriba un numero: '))
print('¡Bien hecho, muggle! Eres libre ahora')

"""
"""
for i in range(2, 8):
    print("El valor de i es actualmente", i)
    
"""
"""
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2
"""
""""
import time

for i in range(6):
    print('Mississippi', i)
    time.sleep(1)

print('¡Listos o no, ahí voy!')
"""
"""
# Te muestra el numero mas grande, Utilizando BREAK!!
largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
"""
"""
# Te muestra el numero mas grande, Utilizando CONTINUE!!
largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
"""
"""
while True:
    palabra = input('Ingrese una palabra: \n')

    if palabra == 'chupacabra':
        break

print('¡Has dejado el bucle con éxito')
"""
"""
palabraSinVocal = ""
vocales = 'AEIOU'
# Indicar al usuario que ingrese una palabra
userWord = input("Ingrese algo:")

# y asignarlo a la variable userWord
userWord = userWord.upper()

for letra in userWord:
    # Completa el cuerpo del ciclo.
    if letra in vocales:
        continue
    else:
        print(letra + palabraSinVocal, end="")
"""
"""
blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#

while True:


print("La altura de la pirámide:", height)

blocks = int(input("Enter the number of blocks: "))

height = 0

inlayer = 1

while inlayer <= blocks:
    height += 1
    blocks -= inlayer  # Esta línea de código funciona distinto a la de arriba y abajo?
    inlayer += 1

print("The height of the pyramid: ", height)
"""
"""
numero = int(input('Ingresa un numero: '))

pasos = 0


while numero > 1:
    if numero % 2 == 0:
        numero = numero / 2
    else:
        numero = (numero * 3) + 1
    pasos += 1
    print(int(numero))
print('Pasos: ', pasos)
"""
"""
#Contador 0 a 10

for i in range(1, 11):
    print('Numero ', i)
"""
"""
#Imprima num Impares
x = 1
while x < 11:
    if x % 2 != 0:
        print('Numero ', x)
    x += 1
"""
"""
#Imprima lo anterior a @
che = ""

for ch in'john.smith@pythoninatitute.org':
    if ch == '@':
        break
    elif ch == '.':
        ch = ' '
    print(ch, end="")
"""
"""
#Omitir el 0
print('Numero es :')

for digit in '0165031806510':
    if digit == '0':
        continue
    print(digit, end='')
"""
"""
# Empieza en 4 hasta 0
n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
"""
"""
#En rango de 4, asta llegar a -1

n = range(4)

for num in n: #Es el rango y num toma la pocición de cada numero
    print(num - 1) # Va descontando
else:
    print(num) #Cuando termina agrega uno mas
"""
"""
#Imprime en rango y salto 

for i in range(0, 6, 3): 
    print(i) #Imprime 0, 3. El 6, no lo muestra porque esta dentro del rango.
"""
"""
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
print('Mi array original es: ', hat_list)

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.

value = int(input('Ingrese un numero: '))

hat_list[2] = value

print('Se modifico el array, cambiando el numero del medio ', hat_list)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

print('Se elimina el ultimo numero de la lista', hat_list[-1])

del hat_list[-1]


# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

print('El numero de elementos de la lista es: ', len(hat_list))

print(hat_list)
"""
"""
#Utilizar append
my_list = []  # Creando una lista vacía.

for i in range(5):
    
    my_list.append(i + 1)

print(my_list)
# [1, 2, 3, 4, 5]
"""
"""
#Utilizar insert
my_list = []  # Creando una lista vacía.

for i in range(5):
    #Va a comenzar en el 1 y va a 
    #correrse hacia la derecha.
    my_list.insert(0, i + 1)

print(my_list)
#[5, 4, 3, 2, 1]
"""
"""
#Intercambiar valores

variable_1 = 1
variable_2 = 2

#Metodo en python
variable_1, variable_2 = variable_2, variable_1

print(variable_1, variable_2)
"""
"""
#Intercambiar numeros en Array
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):#Se utiliza // 2, para que tanto los inpares como los pares se intercambien 
                            # si, nose ponen, el impar de medio queda en el lugar 
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
"""
"""
Paso 1: Crea una lista vacía llamada beatles.
Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
Paso 3: Emplea el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
"""
"""
# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
Beatles.append('John Lennon')
Beatles.append('Paul McCartney')
Beatles.append('George Harrison')
print("Paso 2:", Beatles)

# paso 3

for i in range(2):
    Beatles.insert(i, str(input('Ingrese un nombre: ')))
    i += 1
print("Paso 3:", Beatles)

# paso 4
num = 0
for i in range(2):
    print('El array es: ', Beatles)
    num = int(input('Ingresa numero del indice (0 al 4) a eliminar: '))
    del Beatles[num]
    i += 1
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0, 'Ringo Starr')
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))
"""
"""

#Imprime el array
num = [1, 2, 3, 4]

for i in num:
    print(i)
"""
"""
#Ordenar una lista de array
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
"""
"""
#Ordenar una lista de array, con un comando 
my_list = []
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

my_list.sort()

print("\nOrdenada:")
print(my_list)
"""
"""
#No repetir numeros

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

#
# Escribe tu código aquí.
#

for i in my_list:
    if i in my_list:
        del my_list[i]
    i += 1
my_list.sort()

print("La lista con elementos únicos:")
print(my_list)
"""
"""
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("La temperatura más alta fue:", highest)
"""
"""
def is_year_leap(year):
	if year < 1582:
		return False
	elif year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
"""
"""
def is_year_leap(year):
	if year < 1582:
		return False
	elif year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year, month):
	cantidMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if is_year_leap(year):
		month == 2
		return 29

	return cantidMes[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
"""
"""
def is_year_leap(year):
	if year < 1582:
		return False
	elif year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year, month):
	cantidMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if is_year_leap(year) and month == 2:
		return 29

	return cantidMes[month - 1]

def day_of_year(year, month, day):
	if year < 1582:
		return None
	if month > 31 or month < 1:
		return None
	if day > 31 or day < 1:
		return None
	totaldia = day
	month = month - 1
	while month > 0:
		totaldia += days_in_month(year, month)
		month -= 1
	return totaldia


print(day_of_year(2000, 1, 31))
"""
"""
#Numero primos

def is_prime(num):
	divisor = 2
	while divisor < num:
		if num % divisor == 0:
			return False
		divisor += 1
	return True
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
"""
"""
#Conversor de unidades

def liters_100km_to_miles_gallon(liters):
	millasPorGallon = 235.21 / liters
	return millasPorGallon


def miles_gallon_to_liters_100km(miles):
	litrosCadacienkm = 235.21 / miles
	return litrosCadacienkm


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
"""
"""
def is_prime(num):
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
"""


