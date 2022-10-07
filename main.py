class Administrador():
    def __init__(self, adminUsuario):
        self.adminUsuario = adminUsuario


class Libro():
    def __init__(self, codigo, nombre, autor, stock, edicion):
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.stock = stock
        self.edicion = edicion
        self.pedido = False

    def pedirLibro(self):
        self.pedido = True
        pass

    def devolverLibro(self):
        pass

    def reservarLibro(self):
        pass


class Literarios(Libro):
    def __init__(self, codigo, nombre, autor, stock, edicion, genero, editorial):
        super().__init__(codigo, nombre, autor, stock, edicion)
        self.genero = genero
        self.editorial = editorial


class Academicos(Libro):
    def __init__(self, codigo, nombre, autor, stock, edicion, rama, editorial):
        super().__init__(codigo, nombre, autor, stock, edicion)
        self.rama = rama
        self.editorial = editorial


class Empleado():
    def __init__(self, empleadoUsuario):
        self.empleadoUsuario = empleadoUsuario

    def agregarUsuario(self):
        pass

    def eliminarUsuario(self):
        pass

    def modificarUsuario(self):
        pass


class Cliente():
    def __init__(self, tipo):
        self.tipo = tipo


class Institucion(Cliente):
    def __init__(self, tipo, nombreInstitucion):
        super().__init__(tipo)
        self.nombreInstitucion = nombreInstitucion


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


# inputs de datas


_ad = "clave"
ad = ""

while (ad != _ad):
    ad = input("ingrese la clave: ")

Adimin = Administrador(ad)
b = input("El libro a prestar es para? (instituto o persona):")
if b == "instituto":
    nom = input("nombre de institucion: ")
    inst = Institucion(b, nom)
    cla = input(
        "indique la clase del libro que quiere [literarios/académicos]:")
    cod = int(input("codigo: "))
    nom = input("nombreLibro: ")
    aut = input("autor: ")
    stock = input("stock:")
    edicion = input("edicion: ")
    genero = input("genero: ")
    editotial = input("editotial: ")

    if cla == "literarios":
        liter = Literarios(cod, nom, aut, stock, edicion, genero, editotial)
        print("Se ha guardado con éxito")
    else:
        liter = Academicos(cod, nom, aut, stock, edicion, genero, editotial)
        print("Se ha guardado con éxito")
else:
    nom = input("nombre: ")
    mem = input("membresia: ")
    edad = input("edad: ")
    cant = input("cantidad: ")
    dni = input("dini: ")
    persona1 = Persona(nom, mem, edad, dni, cant)
    print(persona1.mostrarDatos())
