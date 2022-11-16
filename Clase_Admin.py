from tkinter import ttk
from tkinter import *
from Funciones_DB import *
from abc import ABC, abstractmethod

class I_Clases(ABC):
    @abstractmethod
    def ventanaPrincipal(self):
        pass

    @abstractmethod
    def consultar(self, consulta, parametros):
        pass

class VentanaPrincipal():
    def __init__(self):
        self.raiz = Tk()
        
class Admin(VentanaPrincipal, I_Clases):

    db_nombre = "StockLibros.db"

    def __init__(self):
        super().__init__()
        self.wind = self.raiz
        self.wind.title('Sistema bibliotecario')
        self.wind.geometry("600x300")
        self.wind.config(bg = "brown")
        self.wind.columnconfigure(0, weight = 1)
        self.wind.rowconfigure(0, weight = 1)

    def agregarProducto(self):
        cuadro = LabelFrame(self.wind, text = 'Ingrese el libro deseado: ')
        cuadro.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        #IngresarCodigo
        Label(cuadro, text = 'Codigo: ').grid(row = 1, column = 0)
        self.codigo = Entry(cuadro)
        self.codigo.focus()
        self.codigo.grid (row = 1, column = 1)
        #IngresarNombre
        Label(cuadro, text = 'Nombre: ').grid(row = 2, column = 0)
        self.nombre= Entry(cuadro)
        self.nombre.grid (row = 2, column = 1)
        #IngresarAutor
        Label(cuadro, text = 'Autor: ').grid(row = 3, column = 0)
        self.autor = Entry(cuadro)
        self.autor.grid(row = 3, column = 1)
        #IngresarStock
        Label(cuadro, text = "Stock: ").grid(row = 4, column = 0)
        self.stock = Entry(cuadro)
        self.stock.grid(row=4, column=1)
        #BotónAgregarProducto
        self.principal.destroy()
        Button(cuadro, text = 'Agregar', height = 2, command = lambda: Funciones_Admin_Db.agregarProductos(self)).grid(row = 5, columnspan = 2, sticky = W + E)
        
    def eliminarProducto(self):
        cuadro2 = LabelFrame(self.wind, text = 'Codigo del libro que desea eliminar del stock: ')
        cuadro2.grid(row = 0, column = 0, columnspan = 3, pady = 40)
        #IngresarCodigo
        Label(cuadro2, text = 'Codigo: ').grid(row = 1, column = 0)
        self.codigo = Entry(cuadro2)
        self.codigo.focus()
        self.codigo.grid (row = 1, column = 1)
        self.principal.destroy()
       #BotónBorrarProducto
        Button(cuadro2, text = 'Borrar', height = 1, command = lambda: Funciones_Admin_Db.borrarProductos(self)).grid(row = 5, columnspan = 4, sticky = W + E)

    def modificarStock(self):
        cuadro3 = LabelFrame(self.wind, text = "Ingrese el codigo y el nuevo stock: ")
        cuadro3.grid(row = 0, column = 0, columnspan = 2, pady = 40)
        #IngresarCodigo:
        Label(cuadro3, text = 'Codigo: ').grid(row = 1, column = 0)
        self.codigo = Entry(cuadro3)
        self.codigo.focus()
        self.codigo.grid (row = 1, column = 1)
        Label(cuadro3, text = "Stock: ").grid(row = 2, column = 0)
        self.stock = Entry(cuadro3)
        self.stock.grid(row=2, column=1)
        self.principal.destroy()
        #BotonBorrarStock
        Button(cuadro3, text = "Modificar Stock", command = lambda: Funciones_Admin_Db.editarStock(self)).grid(row=4, columnspan = 4, sticky = W + E)

    def mostrarStock(self):
        cuadro4 = LabelFrame(self.wind, text = "El stock disponible es el siguiente: ")
        #TablaDeProductos
        self.Tabla = ttk.Treeview(columns = (1,2,3), padding = "0", height = 10)
        self.wind.geometry("800x600")
        self.Tabla.grid(row=0, column=0, columnspan=2)
        self.Tabla.heading("#0", text = "Codigo", anchor=CENTER)
        self.Tabla.heading("#1", text = "Nombre", anchor=CENTER)
        self.Tabla.heading("#2", text = "Autor", anchor=CENTER)
        self.Tabla.heading("#3", text = "Stock", anchor=CENTER)
        Funciones_Admin_Db.Traer(self)
        self.principal.destroy()

    def ventanaPrincipal(self):
        Principal = LabelFrame(self.wind, text = "Ingrese la opcion deseada: ")
        self.principal = Principal
        Principal.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        Button(Principal, text = "Agregar Libro", height = 2, width = 50, command = lambda : self.agregarProducto()).grid(row = 1, columnspan = 2, sticky = W + E)
        Button(Principal, text = "Eliminar Libro", height = 2, command = lambda : self.eliminarProducto()).grid(row = 2, columnspan = 2, sticky = W + E)
        Button(Principal, text = "Modificar Stock", height = 2, command = lambda : self.modificarStock()).grid(row=3, columnspan = 2, sticky = W+E)
        Button(Principal, text = "Mostrar Libros en Stock", command = lambda: self.mostrarStock(), height = 2).grid(row=4, columnspan=2, sticky = W + E)
    
        self.raiz.mainloop()

    def validarProductos(self):
        return len(self.codigo.get()) and len(self.nombre.get()) != 0 and len(self.autor.get()) != 0 and len(self.stock.get()) 

    def validarStock(self):
        return int(self.stock.get()) > 0
    
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
    
    