from tkinter import ttk
from tkinter import *
import sqlite3 as sql


class VentanaPrincipal():
    def __init__(self):
        self.raiz = Tk()
        
class Admin(VentanaPrincipal):

    db_nombre = "BaseDatos2.db"

    def __init__(self):
        super().__init__()
        self.wind = self.raiz
        self.wind.title('Sistema bibliotecario')
        self.wind.geometry("600x300")
        self.wind.config(bg = "brown")
        self.wind.columnconfigure(0, weight = 1)
        self.wind.rowconfigure(0, weight = 1)
        

    def cambiar(self, frame):
        try:
            frame.tkraise()
        except:
            pass
        
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
        Button(cuadro, text = 'Agregar', height = 2, command = self.agregarProductos).grid(row = 5, columnspan = 2, sticky = W + E)
        cuadro.tkraise()
        
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
        Button(cuadro2, text = 'Borrar', height = 1, command = self.borrarProductos).grid(row = 5, columnspan = 4, sticky = W + E)
        cuadro2.tkraise()

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
        Button(cuadro3, text = "Modificar Stock", command = self.editarStock).grid(row=4, columnspan = 4, sticky = W + E)

    def ventanaPrincipal(self):
        Principal = LabelFrame(self.wind, text = "Ingrese la opcion deseada: ")
        self.principal = Principal
        Principal.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        Button(Principal, text = "Agregar Libro", height = 2, width = 50, command = lambda : self.cambiar(self.agregarProducto())).grid(row = 1, columnspan = 2, sticky = W + E)
        Button(Principal, text = "Eliminar Libro", height = 2, command = lambda : self.cambiar(self.eliminarProducto())).grid(row = 2, columnspan = 2, sticky = W + E)
        Button(Principal, text = "Modificar Stock", height = 2, command = lambda : self.cambiar(self.modificarStock())).grid(row=3, columnspan = 2, sticky = W+E)
        Button(Principal, text = "Mostrar Libros por consola", height = 2, command = self.Traer).grid(row=4, columnspan=2, sticky = W + E)
    
        self.raiz.mainloop()

    def consultar(self, query, parameters = ()):
        with sql.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result 

    def validarProductos(self):
        return len(self.codigo.get()) and len(self.nombre.get()) != 0 and len(self.autor.get()) != 0 and len(self.stock.get()) 

    def validarStock(self):
        return int(self.stock.get()) > 0

    #Consulta a la base de datos
    def Traer(self):
        query = 'SELECT * FROM Libros ORDER BY Codigo ASC'
        db_filas = self.consultar(query)
        for fila in db_filas:
            print (fila)
        print("Libros presentes en el stock.")

    #Agregar Productos (no stock como tal)
    def agregarProductos(self):
        if self.validarProductos():
            query = 'INSERT or IGNORE INTO Libros VALUES(?, ?, ?, ?)'
            parametros = (self.codigo.get(), self.nombre.get(), self.autor.get(), self.stock.get())
            self.consultar(query, parametros)
            print("Los datos han sido guardados.")
        else:
            print("Los campos son requeridos.")
    #Borrar el producto de una lista
    def borrarProductos(self):
        borrar = self.codigo.get()
        query = "DELETE FROM Libros WHERE Codigo = ?"
        self.consultar(query, (borrar))
        print("Los datos han sido borrados.")
    
    def editarStock(self):
        if self.validarStock():
            parametros = (self.stock.get(), self.codigo.get())
            query = "UPDATE Libros SET Stock = ? WHERE Codigo = ?"
            self.consultar(query, parametros)
            print("El stock ha sido modificado.")
        else:
            print("Se requiere un stock mayor a cero.")

def home():
    app = Admin()
    app1 = Admin.ventanaPrincipal(app)
  
