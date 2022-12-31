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
        opcion = int(input("Ingrese la opcion que desee --> "))

        if opcion == 1: 
            AgregarCliente.agregarCliente(self)
        elif opcion == 2:
            EliminarCliente.eliminarCliente(self)
        elif opcion == 3:
            ModificarCliente.modificarNivel(self)
        else:
            print("Ingrese una opcion valida.")

class Funciones_Cliente_Db():
    def PedirLibro(self):
        query = "SELECT Stock from Libros WHERE Codigo = ?"
        stock = self.consultar(query, [self.codigo])
        from FuncionesLibro.Funciones_Libro import Buscar
        membresia = Buscar.buscarMembresia(self)
        try:
            for stocks in stock:
                stock_nuevo = ''.join(str(i) for i in stocks)
            if int(stock_nuevo) >= 1:
                query_2 = "UPDATE Libros SET Stock = Stock - 0.5 WHERE Stock > 0 and Codigo = ?"
                self.consultar(query_2, self.codigo)
                print("El libro ha sido entregado, recuerde entregarlo a tiempo.")
                if (membresia == 1):
                    print("Tiene un plazo de 7 dias para devolverlo a la biblioteca.")
                elif (membresia == 2):
                    print("Tiene un plazo de 14 dias para devolverlo a la biblioteca.")
                else:
                    print("Tiene un plazo de 30 dias para devolverlo a la biblioteca.")
            else:
                print("El libro no se encuentra disponible, considere hacer una reserva.")
        except:
            print("Se ha colocado un codigo no existente.")