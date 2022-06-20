"""
Ejercicio 1
Año bisiesto
"""
año = int(input('Ingrese el año'))
resultado = None
if (año % 4 == 0 and año % 100 != 0 or año % 400 == 0):
    resultado = 'Año bisiesto'
else:
    resultado = 'Año no bisiesto'
print(f'El año que ingreso es {año} y es {resultado}')
