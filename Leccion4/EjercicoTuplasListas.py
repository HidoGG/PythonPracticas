import math #Importamos la clase math hacer uso de la función sqrt(raiz cuadrada)

#Ejercicio

numero = int(input('Digite un numero positivo'))
while numero < 0:
    print('Error -> Debera ser un numero positivo')
    numero = int(input('Degite un numero positivo'))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')



