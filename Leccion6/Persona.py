class Persona: #Creamos una clase
    #self, solo se encuntra dentro de los metodos
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
        #Argumentos variables *args y **kwargs
        #Son del tipo Publico los atributos
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni  #Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual a this
        print(f'la clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')



persona1 = Persona('Ariel', 'Betancud', 355855,40) # Nesecitamos enviar argumentos
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini', 3556885, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

#persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o darpa error

persona1.telefono = '4445555289'
print(f'este es el telefono de: {persona1.nombre} {persona1.telefono}') #Hemos creado un atributo de un objeto

# Modificar datos
persona1.nombre = 'Liliana'
persona1.apellido ='Buccella'
persona1.edad = 40
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()


# print(persona2.telefono) El objeto persona2 no tiene este atributo, da error

persona3 = Persona('Rogelio', 'Roman', 5899666, 22, 'telefono', '25366588', 'Calle Lopez', 823,'manzana', 77,'casa', 18, altura=1.83, peso=105, CFavorito='Azul', auto='Citron', modelo=2015)
persona3.mostrar_detalle()

#print(persona3._dni) #Esto no se debe utilizar (Esta encapsulado) en python, esto dice que lo desconocemos

#persona3.__nombre #Esta totalmente encapsulado (Cuando se le pone "__")
