import sqlite3 as sql

class Funciones_Admin_Db():

    def Traer(self):
        query = 'SELECT * FROM Libros ORDER BY Codigo ASC'
        db_filas = self.consultar(query)
        for fila in db_filas:
            print(fila)
    
    def agregarProductos(self):
        query = 'INSERT or IGNORE INTO Libros VALUES(?, ?, ?, ?)'
        parametros = (self.codigo, self.nombre, self.autor, self.stock)
        self.consultar(query, parametros)
        print("Los datos han sido guardados.")

    def borrarProductos(self):
        borrar = self.codigo
        query = "DELETE FROM Libros WHERE Codigo = ?"
        self.consultar(query, [borrar])
        print("Los datos han sido borrados.")
    
    def editarStock(self):
        parametros = (self.stock, self.codigo)
        query = "UPDATE Libros SET Stock = ? WHERE Codigo = ?"
        self.consultar(query, parametros)
        print("El stock ha sido modificado correctamente.")
    