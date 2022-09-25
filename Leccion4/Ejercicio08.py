# Ejercicio 8: Menú interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo
# inicial de 1000$ y tendrá el siguinte menú de opciones:
#                 1. Ingresar dinero en la cuenta
#                 2. Retirar dinero de la cuenta
#                 3. Mostrar dinero disponible
#                 4. Salir

saldo = 1000
bandera = True
while bandera:
    print('Cajero Automatico')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    num = int(input('Ingrese numero del menu'))
    num1 = 0
    for i in range(1, 4):
        i = num
        if num == 1:
            num1 = int(input('Ingrese saldo a depositar: '))
            saldo = saldo + num1
            print(f'{saldo}')
            break
        elif num == 2:
            num1 = int(input('Ingrese saldo a retirar: '))
            saldo = saldo - num1
            print(f'{saldo}')
            break
        elif num == 3:
            print(f'Su saldo es {saldo}')
            break
        elif num == 4:
            bandera = False
            break











