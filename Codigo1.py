from tkinter import ttk
from tkinter import *
import sqlite3 as sql

class Admin():

    db_nombre = "BaseDatos.db"

    def __init__(self, window):
        self.wind = window
        self.wind.title('Sistema bibliotecario')

    def editarStock(self):
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
        ttk.Button(cuadro, text = 'Agregar', command = self.agregarProductos).grid(row = 4, columnspan = 2, sticky = W + E)

        self.Traer()

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
       
if __name__ == "__main__":
    window = Tk()
    app = Admin(window)
    app1 = Admin.editarStock(app)
    window.mainloop()

