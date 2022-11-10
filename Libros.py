from tkinter import ttk
from tkinter import *
import sqlite3 as sql
#from PIL import ImageTk, Image

class VentanaPrincipal():
    def __init__(self):
        self.raiz = Tk()
        
class Admin(VentanaPrincipal):

    db_nombre = "StockLibros.db"

    def __init__(self):
        super().__init__()
        self.wind = self.raiz
        self.wind.title('Sistema bibliotecario')
        self.wind.geometry("600x400+500+250")
        self.wind.columnconfigure(0, weight = 1)
        self.wind.rowconfigure(0, weight = 1)
        """
        canva = Canvas(self.wind, width = 1000, height = 600, bg="yellow")
        canva.grid(row = 2, column = 2)
        self.Imagen = ImageTk.PhotoImage(Image.open("fondo_library.png"))
        canva.create_image(0,20, image = self.Imagen, anchor = "nw")"""

    def cambiar(self, frame):
        try:
            frame.tkraise()
        except:
            print("El ")
            

    def agregarStock(self):
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
        #BotónAgregarProducto
        self.principal.destroy()
        ttk.Button(cuadro, text = 'Agregar', command = self.agregarProductos).grid(row = 4, columnspan = 2, sticky = W + E)

        """
        #BotonEditarProducto
        ttk.Button(text = "Editar").grid(row=5, column=1, sticky = W + E)"""
        cuadro.tkraise()
        
        """self.Traer()"""
    def eliminarStock(self):
        cuadro2 = LabelFrame(self.wind, text = 'Codigo del libro que desea eliminar del stock: ')
        cuadro2.grid(row = 0, column = 0, columnspan = 3, pady = 40)
        #IngresarCodigo
        Label(cuadro2, text = 'Codigo: ').grid(row = 1, column = 0)
        self.codigo = Entry(cuadro2)
        self.codigo.focus()
        self.codigo.grid (row = 1, column = 1)
        self.principal.destroy()
       #BotónBorrarProducto
        ttk.Button(cuadro2, text = 'Borrar', command = self.borrarProductos).grid(row = 5, columnspan = 4, sticky = W + E)
        cuadro2.tkraise()

    def ventanaPrincipal(self):
        Principal = LabelFrame(self.wind, text = "Ingrese la opcion deseada: ")
        self.principal = Principal
        Principal.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        ttk.Button(Principal, text = "Agregar Stock", command = lambda : self.cambiar(self.agregarStock())).grid(row = 1, columnspan = 2, sticky = W + E)
        ttk.Button(Principal, text = "Eliminar Stock", command = lambda : self.cambiar(self.eliminarStock())).grid(row = 2, columnspan = 2, sticky = W + E)
        ttk.Button(Principal, text = "Editar Stock").grid(row = 3, columnspan = 2, sticky = W + E)
    
        self.raiz.mainloop()

    def consultar(self, query, parameters = ()):
        with sql.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result 

    def Traer(self):
        query = 'SELECT * FROM Libros ORDER BY Codigo ASC'
        db_filas = self.consultar(query)
        for fila in db_filas:
            print (fila)

    def validarProductos(self):
        return len(self.codigo.get()) and len(self.nombre.get()) != 0 and len(self.autor.get()) != 0 

    def agregarProductos(self):
        if self.validarProductos():
            query = 'INSERT or IGNORE INTO Libros VALUES(?, ?, ?)'
            parametros = (self.codigo.get(), self.nombre.get(), self.autor.get())
            self.consultar(query, parametros)
            print("Los datos han sido guardados.")
        else:
            print("Los campos son requeridos.")
    
    def borrarProductos(self):
        borrar = self.codigo.get()
        query = 'DELETE FROM Libros WHERE Codigo = ?'
        self.consultar(query, [borrar])
        print("Los datos han sido borrados.")