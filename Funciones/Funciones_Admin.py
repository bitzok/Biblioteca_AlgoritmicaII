from Clase_Admin import Admin
from Funciones_DB import *
from Funciones.Interfaces_Admin import *

class AgregarProducto(Admin, AddProduct):
    def __init__(self):
        super().__init__()

    def agregarProducto(self):
        self.codigo =  int(input("Ingrese el codigo del nuevo libro: "))
        self.nombre =  str(input("Ingrese el nombre del nuevo libro: "))    
        self.autor = str(input("Ingresar el autor del nuevo libro: "))
        self.stock = int(input("Ingresar el stock del nuevo libro: "))
        if self.codigo > 0 and len(self.nombre) != 0 and len(self.autor) != 0 and self.stock > 0:
            Funciones_Admin_Db.agregarProductos(self)
        else:
            print("Ingrese correctamente los campos solicitados.")
        VolverMenuPrincipal.volverMenu(self)

class EliminarProducto(Admin, RemoveProduct):
    def __init__(self):
        super().__init__()

    def eliminarProducto(self):
        self.codigo =  int(input("Ingrese el codigo del libro a eliminar: "))
        if self.codigo > 0:
            Funciones_Admin_Db.borrarProductos(self)
        else:
            print("Ingrese correctamente el campo solicitado.")
        VolverMenuPrincipal.volverMenu(self)

class ModificarProducto(Admin, ModifyProduct):
    def __init__(self):
        super().__init__()

    def modificarProducto(self):
        self.codigo =  int(input("Ingrese el codigo del libro: "))
        self.stock = int(input("Ingresar el nuevo stock del libro: "))
        if self.codigo > 0 and self.stock > 0:
            Funciones_Admin_Db.editarStock(self)
        else:
            print("Ingrese correctamente los campos solicitados.")
        VolverMenuPrincipal.volverMenu(self)

class MostrarStock(Admin, ShowStock):
    def __init__(self):
        super().__init__()

    def mostrarStock(self):
        print("Se mostrará el stock disponible: ")
        Funciones_Admin_Db.Traer(self)
        VolverMenuPrincipal.volverMenu(self)

class VolverMenuPrincipal(Admin, BackToMenu):
    def __init__(self):
        super().__init__()

    def volverMenu(self):
        print("Desea volver al menu principal?")
        opcion = int(input("1 para Sí, 2 para No."))
        if opcion == 1:
            VentanaPrincipal.ventanaPrincipal(self)
        else:
            print("Hasta luego.")
        
class VentanaPrincipal(Admin, Menu):
    def __init__(self):
        super().__init__()

    def ventanaPrincipal(self):
        print("1. Agregar Productos.")
        print("2. Eliminar Productos.")
        print("3. Modificar Stock.")
        print("4. Mostrar Stock.")
        opcion = int(input("Ingrese la opcion que desee:"))

        if opcion == 1:
            AgregarProducto.agregarProducto(self)
        elif opcion == 2:
            EliminarProducto.eliminarProducto(self)
        elif opcion == 3:
            ModificarProducto.modificarProducto(self)
        elif opcion == 4:
            MostrarStock.mostrarStock(self)
        else:
            print("Opcion invalida.")