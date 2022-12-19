from Funciones_DB import *
from Funciones.Interfaces_Admin import *


class Buscar(Atributos):
    def __init__(self):
       super().__init__()
    
    def buscarLibro(self):
        self.nombres = input("Ingrese el nombre del libro a buscar: ")
        Funciones_Admin_Db.BuscarLibro(self)
        VolverMenuPrincipal.volverMenu(self)

class Pedir(Atributos):
    def __init__(self):
        super().__init__()
    
    def pedirLibro(self):
        self.codigo = input("Ingrese el codigo del libro a pedir: ")
        Funciones_Admin_Db.PedirLibro(self)
        VolverMenuPrincipal.volverMenu(self)
class Reserva(Atributos):
    def __init__(self):
        super().__init__()

    def reservarLibro(self):
        self.codigo = input("Ingrese el codigo del libro a reservar: ")
        Funciones_Admin_Db.ReservarLibro(self)
        VolverMenuPrincipal.volverMenu(self)

class VentanaPrincipal(Atributos):
    def __init__(self):
        super().__init__()

    def ventanaPrincipal(self):
        if self.cond == 0:
            VerificarCliente.verificarDNI(self)
       
        if self.VerificarIdentidad:
            self.cond = 1
            print("1. Consultar disponibilidad del libro.")
            print("2. Pedir libro.")
            print("3. Reservar libro.")
            opcion = int(input("Ingrese la opcion que desee:"))

            if opcion == 1:
                Buscar.buscarLibro(self)
            elif opcion == 2:
                Pedir.pedirLibro(self)
            elif opcion == 3:
                Reserva.reservarLibro(self)
            else:
                print("Opcion invalida.")
        else:
            print("Primero registre al cliente en el sistema de Clientes.")

class VolverMenuPrincipal(Atributos):
    def __init__(self):
        super().__init__()

    def volverMenu(self):
        print("Desea volver al menu principal?")
        opcion = int(input("1 para Sí, 2 para No."))
        if opcion == 1:
            VentanaPrincipal.ventanaPrincipal(self)
        else:
            print("Hasta luego.")

class VerificarCliente(Atributos):
    def __init__(self):
        super().__init__()
    
    def verificarDNI(self):
        print("Ingrese el DNI del cliente para verificar si se encuentra en la base de datos.")
        self.identidad = int(input("Ingrese el DNI: "))
        self.VerificarIdentidad = Funciones_Admin_Db.VerificarDNI(self)