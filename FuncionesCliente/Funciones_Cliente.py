from Funciones_DB import *
from FuncionesCliente.Interfaces_Cliente import *

from werkzeug.security import generate_password_hash, check_password_hash

class AgregarCliente(Atributos, AddProduct):
    def __init__(self):
        super().__init__()

    def agregarCliente(self):
        self.nombre =  str(input("Ingrese el Nombre del nuevo cliente: "))
        self.apellido =  str(input("Ingrese el Apellido del nuevo cliente: "))
        self.dni = 'x'
        self.membresia = 0
        self.tarjeta1 = 'x'
        self.digver = 54

        while len(self.dni) != 8 or self.dni.isdigit() != True: 
            self.dni = str(input("Ingresar el DNI del nuevo cliente: "))

        while self.membresia<1 or self.membresia>3: 
            self.membresia = int(input("Ingresar el Nivel de mebresia del nuevo cliente: "))

        while len(self.tarjeta1) < 13 or len(self.tarjeta1) > 15 or self.tarjeta1.isdigit() != True:
            self.tarjeta1 = str(input("Ingresar la tarjeta del  cliente por favor: "))

        self.fechaexp = str(input("Ingresar la fecha de expiración de la tarjeta (XX/ZZ): "))

        while self.digver<100 or self.digver>999: 
            self.digver = int(input("Ingresar los 3 dígitos verificador del cliente: "))

        self.tarjeta = generate_password_hash(self.tarjeta1, 'sha256', 10)

        Verificacion = Funciones_Admin_Db.VerificarDNIs(self)

        if Verificacion == True:
            Funciones_Admin_Db.agregarClientes(self)
        else:
            print("Ya existe un usuario registrado con ese DNI")
        
        VolverMenuPrincipal.volverMenu(self)

class EliminarCliente(Atributos, RemoveProduct):
    def __init__(self):
        super().__init__()

    def eliminarCliente(self):
        self.dni =  str(input("Ingrese el DNI del Cliente a eliminar: "))

        if len(self.dni) != 0:
             Funciones_Admin_Db.borrarClientes(self)
        else:
            print("Ingrese correctamente el campo solicitado.")
        VolverMenuPrincipal.volverMenu(self)


class ModificarCliente(Atributos, ModifyProduct):
    def __init__(self):
        super().__init__()

    def modificarNivel(self):
        self.dni =  str(input("Ingrese el DNI del Cliente a modificar: "))
        self.membresia = int(input("Ingresar el nuevo nivel de su mebresía: "))
        if len(self.dni) != 0 and self.membresia > 0:
            Funciones_Admin_Db.editarNivel(self)
        else:
            print("Ingrese correctamente los campos solicitados.")
        VolverMenuPrincipal.volverMenu(self)


class MostrarCliente(Atributos, ShowStock):
    def __init__(self):
        super().__init__()

    def mostrarCliente(self):
        print("Se mostrará Los Clientes: ")
        Funciones_Admin_Db.traerClientes(self)
        VolverMenuPrincipal.volverMenu(self)


class VolverMenuPrincipal(Atributos, BackToMenu):
    def __init__(self):
        super().__init__()

    def volverMenu(self):
        print("Desea volver a las opciones anteriores?")
        opcion2 = int(input("1. Sí, 2. No.\n"))
        if opcion2 == 1:
            VentanaPrincipal.ventanaPrincipal(self)
        else:
            print("Hasta luego.")


class VentanaPrincipal(Atributos, Menu):
    def __init__(self):
        super().__init__()

    def ventanaPrincipal(self):
        print("1. Agregar Cliente.")
        print("2. Eliminar Cliente.")
        print("3. Modificar Nivel del Cliente.")
        print("4. Mostrar Clientes totales.")
        opcion = int(input("Ingrese la opcion que desee --> "))

        if opcion == 1: 
            AgregarCliente.agregarCliente(self)
        elif opcion == 2:
            EliminarCliente.eliminarCliente(self)
        elif opcion == 3:
            ModificarCliente.modificarNivel(self)
        elif opcion == 4: 
            MostrarCliente.mostrarCliente(self)
        else:
            print("Ingrese una opcion valida.")