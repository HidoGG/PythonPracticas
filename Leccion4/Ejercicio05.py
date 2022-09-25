#Ejercicio 5: Facrorial de un número positivo
#Hacer un programa para calcular la factorial de un número positivo



"""
numero = int(input('Digite un número: '))
multi1 = 1
for i in range(1, numero+1):
    multi1 = multi1 * i
print(multi1)
"""

numero = int(input('Digite un número: '))
while numero < 0: #Mientras el numero sea negativo
    print('Error -> El número tiene que ser positivo')
    numero = int(input('Digite un número: '))
factorial = 1
for i in  range(1, numero+1):#La variable para calcular el factorial
    factorial *= i
print(f'\nEl factorial del numero {numero} positivo ingresado es: {factorial}')


