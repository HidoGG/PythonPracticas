"""
Ejercicio 4
Calcular la califaciacion promedio y mas baja de un grupo de 10
alumnos
"""
suma = 0
califBaja = 99999
for i in range(10):
    num = int(input('Digite la calificacion'))
    suma += num
    if num < califBaja:
        califBaja = num
prome = suma / 10
print(f'El promedio de las notas es: {prome} y la calificación mas baja es {califBaja}')
