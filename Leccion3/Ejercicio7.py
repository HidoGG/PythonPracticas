"""
Ejercico 7: Dadas las horas trabajadas de 5 personas y la
tarifa de pago, calcular el salario y la sumatoria de todos los salarios
"""
i = 1


while i <= 5:
    print(f'Salario del empeado {i} ')
    hora = int(input(f'Digite las horas trabajadas: '))
    tarifa = float(input(f'Digite la tarifa de las horas: '))
    suma = hora * tarifa
    i += 1

input(f'La suma de todos los salarios es: {suma}')


