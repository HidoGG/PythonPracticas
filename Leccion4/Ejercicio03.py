#Ejercicio 3: Insertas elementos y ordenarlos
#Pedir numeros y meterlos en una lista, cuando el usuario
#introduzca un numero 0, nuestro programa dejaria de insertar.
#Por ultimo, mostrar los numeros ordenados de menor a mayor


lista = []
salir = False
while not salir: #El not cambia el valor, entonces, Miestras salir sea falso va a seguir ejecutandoce
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)

lista.sort() #La lista esta ordenada con esta función
print(f'\n lista ordenada : \n{lista}')













