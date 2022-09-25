#Ejercicio 4: Sumar numeros pares dentro de un rango.
#Hacer un progrmaa para sumar números pares dentro
#de un rano, por ejemlo:
# sumar números pares del 2 al 30
#suma = 240


numero = int(input('Digite el primer número, del rango: '))
numero1 = int(input('Digite el segundo número del rango: '))
suma = 0
for i in range(numero, numero1+1):#Se agrega el +1, para que llege a 30
    if i % 2 == 0:
        suma += i
print(f'La suma de los números PARES es: {suma}')








