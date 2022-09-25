# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contacto. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendrá el siguinte menú de opciones:
#           1 . Nuevo contacto
#           2 . Borrar contacto
#           3 . Ver contactos existentes
#           4 . Salir

agenda = {}
bandera = True
while bandera:
    print('\t.Agenda telefonica')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    num = int(input('Ingrese numero del menu'))
    if num == 1:
        nombre = input('Digite nombre del contacto: ')
        telefono = input('Digite numero de telefono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente')
        else:
            print('Este nombre de contacto ya existe')
    elif num == 2:
        nombre = input('Cual es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto requerido')
        else:
            print('Este contacto no existe en la agenda')
    elif num == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items(): #Item, me permite ver clave y valor
            print(f'Nombre: {clave}, Telefono: {valor}')
    elif num == 4:
        print('Gracias por utilizar su agenda de contacto')
        bandera = False
        break
    else:
        print('Se equivoco de opción de menú')
        print()
