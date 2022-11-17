from Funciones_DB import *
from abc import ABC, abstractmethod

class I_Clases(ABC):
    @abstractmethod
    def ventanaPrincipal(self):
        pass

    @abstractmethod
    def consultar(self, consulta, parametros):
        pass

    @abstractmethod
    def VolverMenuPrincipal(self):
        pass

class Pedidos(I_Clases):

    db_nombre = "ListaClientes.db"

    def __init__(self):
        self._nombres = None
        self._apellido = None
        self._dni = None
        self._membresia = None


    def agregarCliente(self):
        self.nombre =  str(input("Ingrese el Nombre del nuevo cliente: "))
        self.apellido =  str(input("Ingrese el Apellido del nuevo cliente: "))    
        self.dni = str(input("Ingresar el DNI del nuevo cliente: "))
        self.membresia = int(input("Ingresar el Nivel de mebresia del nuevo cliente: "))

        if len(self.nombre) != 0 and len(self.apellido) != 0 and len(self.dni) != 0 and self.membresia > 0:
            Funciones_Admin_Db.agregarClientes(self)
        else:
            print("Ingrese correctamente los campos solicitados.")
        self.VolverMenuPrincipal()


    def eliminarCliente(self):
        self.dni =  str(input("Ingrese el DNI del Cliente a eliminar: "))

        if len(self.dni) != 0:
             Funciones_Admin_Db.borrarClientes(self)
        else:
            print("Ingrese correctamente el campo solicitado.")
        self.VolverMenuPrincipal()
        

    def modificarNivel(self):
        self.dni =  str(input("Ingrese el DNI del Cliente a modificar: "))
        self.membresia = int(input("Ingresar el nuevo nivel de su mebresía: "))
        if len(self.dni) != 0 and self.membresia > 0:
            Funciones_Admin_Db.editarNivel(self)
        else:
            print("Ingrese correctamente los campos solicitados.")
        self.VolverMenuPrincipal()


    def mostrarCliente(self):
        print("Se mostrará Los Clientes: ")
        Funciones_Admin_Db.traerClientes(self)
        self.VolverMenuPrincipal()


    def ventanaPrincipal(self):
        print("1. Agregar Cliente.")
        print("2. Eliminar Cliente.")
        print("3. Modificar Nivel del Cliente.")
        print("4. Mostrar Clientes totales.")
        opcion = int(input("Ingrese la opcion que desee:"))
       
        if opcion == 1: 
            self.agregarCliente()
        elif opcion == 2:
            self.eliminarCliente()
        elif opcion == 3:
            self.modificarNivel()
        elif opcion == 4: 
            self.mostrarCliente()
        else:
            print("Ingrese una opcion valida.")


    def VolverMenuPrincipal(self):
        print("Desea volver al menu principal?")
        opcion2 = int(input("1. Sí, 2. No."))
        if opcion2 == 1:
            self.ventanaPrincipal()
        else:
            print("Hasta luego.")


    def consultar(self, query, parameters = ()):
        with sql.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result


if __name__ == "__main__":
    app = Pedidos()
    app.ventanaPrincipal()