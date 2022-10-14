from cliente import Cliente

class Persona(Cliente):
    def __init__(self, membresia, nombre, edad, dni, cantidad):
        self.membresia = membresia
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.cantidad = cantidad

    def mostrarDatos(self):
        return f'Datos mostrados: {self.membresia} {self.nombre} {self.edad} {self.dni} {self.cantidad}'


class Defecto(Persona):
    pass


class Plata(Persona):
    pass


class Bronce(Persona):
    pass
