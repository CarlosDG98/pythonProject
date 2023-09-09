class Padre:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def quienSoy(self):
        print('Hola mi nombre es: ', self.nombre)
        print('Tengo: ', self.edad, " años")

    def trabajar(self):
        print('Ahora estoy trabajando')

class Hijo(Padre):
    def __init__(self, nombre, edad):
        Padre.__init__(self, nombre, edad)
        pass