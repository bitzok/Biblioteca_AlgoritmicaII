from Funciones_DB import *
from Funciones.Interfaces_Admin import *

class Buscar(Atributos):
    def __init__(self):
       super().__init__()
    
    def buscarLibro(self):
        self.nombres = input("Ingrese el nombre del libro a buscar: ")
        Funciones_Admin_Db.BuscarLibro(self)
        VolverMenuPrincipal.volverMenu(self)
        """
        query = "SELECT * from Libros WHERE Nombre LIKE '"+str(self._nombres)+"%'" 
        Db_filas = self.consultar(query)
        print("Se han encontrado los siguientes resultados: ")
        for fila in Db_filas:
            print(fila)"""

class Pedir(Atributos):
    def __init__(self):
        super().__init__()
    
    def pedirLibro(self):
        self.codigo = input("Ingrese el codigo del libro a pedir: ")
        Funciones_Admin_Db.PedirLibro(self)
        VolverMenuPrincipal.volverMenu(self)

        """
        parametros = (self.codigo)
        query = "SELECT Stock from Libros WHERE Codigo = ?"
        stock = self.consultar(query, parametros)
        for stocks in stock:
            stock_nuevo = ''.join(str(i) for i in stocks)
        if int(stock_nuevo) >= 1:
            query_2 = "UPDATE Libros SET Stock = Stock - 0.5 WHERE Stock > 0 and Codigo = ?"
            self.consultar(query_2, parametros)
            print("El libro ha sido entregado, recuerde entregarlo a tiempo.")
        else:
            print("El libro no se encuentra disponible, desea reservarlo?")
            opcion_reserva = int(input("1. Sí -- 2. No "))
            if opcion_reserva == 1:
                self.Reservar()
            elif opcion_reserva == 2:
                print("Hasta luego.")
        """
class Reserva(Atributos):
    def __init__(self):
        super().__init__()

    def reservarLibro(self):
        self.codigo = input("Ingrese el codigo del libro a reservar: ")
        Funciones_Admin_Db.ReservarLibro(self)
        """
        parametros = (self.codigo)
        query = "SELECT Nombre from Libros WHERE Codigo = ?"
        nombre = self.consultar(query, parametros)
        for nombres in nombre:
            Reserva = ''.join(str(i) for i in nombres)
        print(f"Ha reservado el siguiente libro: {Reserva}")"""
        VolverMenuPrincipal.volverMenu(self)

class VentanaPrincipal(Atributos):
    def __init__(self):
        super().__init__()

    def ventanaPrincipal(self):
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