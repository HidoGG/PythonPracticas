"""
Ejercicio 5
Sistema de calificaciones
"""
calificacion = float(input('Ingrese su calificación: '))
nota = None
if 9 <= calificacion <= 10:
    nota = 'A'
elif 8 <= calificacion < 9:
    nota ='B'
elif 7 <= calificacion < 8:
    nota ='C'
elif 6 <= calificacion < 7:
    nota ='D'
elif 0 <= calificacion < 6:
    nota ='F'
else:
    nota = "Valor ingresado incorrecto"
input(f'La ingresada {calificacion} y {nota}')

