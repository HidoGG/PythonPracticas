# Ejercicio 9: Mostrar una frase sin espacios y contar su logitud
# Hacer un programa donde el usuario ingrese una frase, se le
# devolverá la misma frase pero sin espacios en blanco, y
# además un contador de cuántos caracter tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo:     frase = vivir por simpre en paz
#              frase final = vivirporsimpreenpaz
#              N° de caracteres = 20


num1 = str(input('Frase: '))
lista = []
for i in num1:
    if i != ' ':
        lista.append(i)
cadena = "".join(lista)

print(f'La frase, sin espacios es: {cadena}.\nEl número de caracteres es: {len(lista)}.')

















