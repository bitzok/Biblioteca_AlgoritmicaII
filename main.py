from administrador import Administrador
from persona import Persona

# inputs de datas

_ad = "clave"
ad = ""

while (ad != _ad):
    ad = input("ingrese la clave: ")

# Adimin = Administrador(ad)
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
