class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado por el " _ "
        #Los encapsulamos, para que solo se puedan acceder
        #con el Getter o Setter
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método Setter
        print('Estamos utilizando el método Set')
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Método Setter
        print('Estamos utilizando el método Set')
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._edad

    @edad.setter
    def edad(self, edad):  # Método Setter
        print('Estamos utilizando el método Set')
        self._edad = edad

    #Destructor de Objetos
    def __del__(self):
        print(f'Persona2:{self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.edad)  # Llamamos al método getter

    # Asigno con el metodo Set
    persona1.nombre = 'Juan Pedro'

    # Muestra con el metodo Get, otra ves
    print(persona1.nombre)

    # Me muestra toda la ingormación, Actualizada con el nuevo nombre
    print(persona1.mostrar_detalle())

    # No se puede hacer, porque esta encapsulado
    # persona1.edad = 40

    # Atributo fead-only seria la edad porque no tiene el metodo set, LO COMENTAMOS ARRIBA
    print(persona1.edad)

    # Tarea crear tres objetos mas utilizando los métodos getter and setter
    # para modificar, y mostrar los cambios con el método mostrar detalles

    # Primer cambio
    # Creación de Objeto (persona2), con su contructor Persona2(......)
    #Visualizo con el Set
    persona2 = Persona2('Gabriel', 'Hidalgo', 31)
    print(persona2.mostrar_detalle())

    #Realizando cambios con el Get
    persona2.nombre = 'Jose'
    persona2.apellido = 'Caruzo'
    persona2.edad = 50
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalle())

    # Segundo cambio
    # Creación de Objeto (persona3), con su contructor Persona2(......)
    # Visualizo con el Set
    persona3 = Persona2('Carlos', 'Chaler', 31)
    print(persona3.mostrar_detalle())

    # Realizando cambios con el Get
    persona3.nombre = 'Norma'
    persona3.apellido = 'gonzales'
    persona3.edad = 30
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalle())

    #Tercer cambio
    #Creación de Objeto (persona4), con su contructor Persona2(......)
    # Visualizo con el Set
    persona4 = Persona2('Matias', 'Hochoner', 31)
    print(persona4.mostrar_detalle())

    # Realizando cambios con el Get
    persona4.nombre = 'Tomas'
    persona4.apellido = 'Carrizo'
    persona4.edad = 20
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalle())

    # Nos va a decir donde se esta ejecutando el comando
    print(__name__)
