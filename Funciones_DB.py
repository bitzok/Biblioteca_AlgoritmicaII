import sqlite3 as sql
import Clase_Admin as Cod

class Funciones_Admin_Db():

    def Traer(self):
        query = 'SELECT * FROM Libros ORDER BY Codigo DESC'
        db_filas = self.consultar(query)
        for fila in db_filas:
            self.Tabla.insert("", 0, text = fila[0], values = (fila[1], fila[2], fila[3]))

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
        self.consultar(query, [borrar])
        print("Los datos han sido borrados.")
    
    def editarStock(self):
        if self.validarStock():
            parametros = (self.stock.get(), self.codigo.get())
            query = "UPDATE Libros SET Stock = ? WHERE Codigo = ?"
            self.consultar(query, parametros)
            print("El stock ha sido modificado.")
        else:
            print("Se requiere un stock mayor a cero.")
