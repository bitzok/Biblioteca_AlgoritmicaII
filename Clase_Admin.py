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

class Admin(I_Clases):

    db_nombre = "StockLibros.db"

    def __init__(self):
        self._codigo = None
        self._nombre = None
        self._autor = None
        self._stock = None

    def agregarProducto(self):
        #IngresarCodigo
        self.codigo =  int(input("Ingrese el codigo del nuevo libro: "))
        #IngresarNombre
        self.nombre =  str(input("Ingrese el nombre del nuevo libro: "))    
        #IngresarAutor
        self.autor = str(input("Ingresar el autor del nuevo libro: "))
        #IngresarStock  
        self.stock = int(input("Ingresar el stock del nuevo libro: "))
        #CondicionalValores
        if self.codigo > 0 and len(self.nombre) != 0 and len(self.autor) != 0 and self.stock > 0:
            Funciones_Admin_Db.agregarProductos(self)
        else:
            print("Ingrese correctamente los campos solicitados.")
        self.VolverMenuPrincipal()
       
        
    def eliminarProducto(self):
        #IngresarCodigo
        self.codigo =  int(input("Ingrese el codigo del libro a eliminar: "))
       #CondicionalValores
        if self.codigo > 0:
            Funciones_Admin_Db.borrarProductos(self)
        else:
            print("Ingrese correctamente el campo solicitado.")
        self.VolverMenuPrincipal()
        
        
    def modificarStock(self):
        #IngresarCodigo:
        self.codigo =  int(input("Ingrese el codigo del libro: "))
        self.stock = int(input("Ingresar el nuevo stock del libro: "))
        if self.codigo > 0 and self.stock > 0:
            Funciones_Admin_Db.editarStock(self)
        else:
            print("Ingrese correctamente los campos solicitados.")
        self.VolverMenuPrincipal()
        
    def mostrarStock(self):
        print("Se mostrará el stock disponible: ")
        Funciones_Admin_Db.Traer(self)
        self.VolverMenuPrincipal()

    def ventanaPrincipal(self):
        print("1. Agregar Productos.")
        print("2. Eliminar Productos.")
        print("3. Modificar Stock.")
        print("4. Mostrar Stock.")
        opcion = int(input("Ingrese la opcion que desee:"))
       
        if opcion == 1: 
            self.agregarProducto()
        elif opcion == 2:
            self.eliminarProducto()
        elif opcion == 3:
            self.modificarStock()
        elif opcion == 4: 
            print("Se mostrara el stock disponible:")
            self.mostrarStock()
        else:
            print("Ingrese una opcion valida.")

    def VolverMenuPrincipal(self):
        print("Desea volver al menu principal?")
        opcion2 = int(input("1 para Sí, 2 para No."))
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
    app = Admin()
    app.ventanaPrincipal()
