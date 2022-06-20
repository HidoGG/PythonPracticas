"""
Ejercicio 4
Etapas de vida
"""
edad = int(input('Ingrese su edad'))
etapa = None
if 0 <= edad < 10:
    etapa ='La infacia es increible y bella'
elif 10 <= edad < 20:
    etapa ='Tienes muchos cambios, y mucho que estudiar'
elif 20 <= edad < 29:
    etapa ='Amor y comienzas a trabajar'
else:
    etapa ='Por descubir' 
print(f'Tu edad es {edad} y {etapa}')
