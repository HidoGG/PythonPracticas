"""
Ejercicio 3:
Calcular la estación del año
"""

mes = int(input('Ingrese el mes del año, entre el 1 al 12'))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = 'verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'invierno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'primavera'
else:
    estacion = 'Fuera de rango'
print(f'El mes ingresado es {mes}, {estacion}')
