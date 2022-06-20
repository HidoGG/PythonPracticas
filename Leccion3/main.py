# Ciclo While (Mientras o durante)
"""
contador = 0
while contador < 78:
    print('Ejecutando el ciclo while', contador)
    contador += 1
else:
    print('Fin del ciclo while')
"""
"""
#Imprimir numero del 0 al 5 con el ciclo while

max = 5
contador = 0
while contador <= max:
    print(contador)
    contador += 1
"""
"""
#Imprimir en decremento 5 a 0 con el ciclo while
min = 1
contador = 5
while contador >= min:
    print(contador)
    contador -=1
"""

#Ciclo for
"""
cadena = 'hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')
"""
#Palabra reservada break
"""
for letra in 'Alemania':
    if letra == "a":
        print(f'letra encontrada: {letra}')
        break 
else:
    print('Fin del ciclo for')
"""
#Palabra reservada continue
#numeros divisibles por dos que den 0
for i in range(6):
    if i % 2 == 0:
        print(f'valor: {i}')
#numeros impares que no de 0
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')



