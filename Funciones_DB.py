import sqlite3 as sql

class Funciones_Admin_Db():
    
    def Traer(self):
        query = 'SELECT * FROM Libros ORDER BY Codigo ASC'
        db_filas = self.consultar(query)
        for fila in db_filas:
            print(fila)

    def traerClientes(self):
        query = 'SELECT * FROM DatosClientes'
        db_filas = self.consultar(query)
        for fila in db_filas:
            print(fila)
    

    def agregarProductos(self):
        query = 'INSERT or IGNORE INTO Libros VALUES(?, ?, ?, ?)'
        parametros = (self.codigo, self.nombre, self.autor, self.stock)
        self.consultar(query, parametros)
        print("Los datos han sido guardados.")

    def agregarClientes(self):
        query = 'INSERT or IGNORE INTO DatosClientes VALUES(?, ?, ?, ?)'
        parametros = (self.nombre, self.apellido, self.dni, self.membresia)
        self.consultar(query, parametros)
        print("Los datos han sido guardados.")    


    def borrarProductos(self):
        borrar = self.codigo
        query = "DELETE FROM Libros WHERE Codigo = ?"
        self.consultar(query, [borrar])
        print("Los datos han sido borrados.")

    def borrarClientes(self):
        borrar = self.dni
        query = "DELETE FROM DatosClientes WHERE DNI = ?"
        self.consultar(query, [borrar])
        print("Los datos han sido borrados.")
    

    def editarStock(self):
        parametros = (self.stock, self.codigo)
        query = "UPDATE Libros SET Stock = ? WHERE Codigo = ?"
        self.consultar(query, parametros)
        print("El stock ha sido modificado correctamente.")

    def editarNivel(self):
        parametros = (self.membresia, self.dni)
        query = "UPDATE DatosClientes SET Membresia = ? WHERE DNI = ?"
        self.consultar(query, parametros)
        print("La membresia ha sido modificado correctamente.")

class Funciones_Login_Db():
    def user_exists(user,passw):
        success = False
        conn = sql.connect("login.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user = ? AND password = ?', (user, passw))
        if cursor.fetchall():
            cursor.execute('SELECT lvl FROM users WHERE user = ? AND password = ?', (user, passw))
            level = cursor.fetchall()
            success=True
            if(success):
                return level
        else:
            print("Usuario no se encuentra registrado")
            return False
        cursor.close()

class Funciones_Signin_Db():
    def search(user):
        conn = sql.connect('login.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user =?', (user,))
        if cursor.fetchall():
            return False
        else:
            return True
        
    def insert(user, password, lvl):
        conn = sql.connect('login.db')
        cursor = conn.cursor()
        instruction = f"INSERT INTO users VALUES ('{user}','{password}','{lvl}')"
        cursor.execute(instruction)
        conn.commit()
        conn.close()