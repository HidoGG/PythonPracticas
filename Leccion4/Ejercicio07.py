# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# número indicado "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos.
import random

"""
comienzo = random.randint(0, 100)
for i in range(20):
    numero = int(input('Digite un número para comenzar el juego: '))
    if numero > comienzo:
        print('Es mayor')
    elif numero < comienzo:
        print('Es menor')
    else:
        print(f'Ganaste, tu nuemro {numero}, es el mismo del aleatorio: {comienzo}')
"""
comienzo = random.randint(0, 100)
contador = 0
while True:
    numero = int(input('Digite un número para comenzar el juego: '))
    contador += 1
    if numero > comienzo:
        print('\tNo es el numero, digita un número menor')
    elif numero < comienzo:
        print('\tNo es el numero, digita un número mayor')
    else:
        print(f'Ganaste, tu nuemro {numero}, es el mismo del aleatorio: {comienzo}')
        break # Rompe el ciclo
print(f'\nEl numero de intentos: {contador}')