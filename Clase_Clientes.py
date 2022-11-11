from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
import sqlite3 as sql

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
        
class Pedidos(VentanaPrincipal):

    db_nombre = "ListaClientes.db"

    def __init__(self):
        super().__init__()
        self.wind = self.raiz
        self.wind.title('Nuevos pedidos')
        self.wind.geometry("600x400+500+250")
        self.wind.columnconfigure(0, weight = 1)
        self.wind.rowconfigure(0, weight = 1)


    def ventanaPrincipal(self):
        Principal = LabelFrame(self.wind, text = "Ingrese la opcion deseada: ")
        self.principal = Principal
        Principal.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        ttk.Button(Principal, text = "Registrar Usuario", command = lambda : self.nuevoUsuario()).grid(row = 1, columnspan = 2, sticky = W + E)
        ttk.Button(Principal, text = "Eliminar Usuario", command = lambda : self.eliminarUsuario()).grid(row = 2, columnspan = 2, sticky = W + E)
        ttk.Button(Principal, text = "Mostrar Usuarios", command = lambda : self.mostrarUsuario()).grid(row = 3, columnspan = 2, sticky = W + E)
    
        self.raiz.mainloop()
            

    def consultar(self, query, parameters = ()):
        with sql.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            cursor.execute(query, parameters) 
            result = cursor.execute(query, parameters)
            conn.commit()
        return result 


    def nuevoUsuario(self):
        cuadro = LabelFrame(self.wind, text = 'Ingrese el nuevo usuario: ')
        cuadro.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        #IngresarNombre
        Label(cuadro, text = 'Nombre: ').grid(row = 1, column = 0)
        self.nombre = Entry(cuadro)
        #self.nombre.focus()
        self.nombre.grid (row = 1, column = 1)
        #IngresarApellido
        Label(cuadro, text = 'Apellido: ').grid(row = 2, column = 0)
        self.apellido= Entry(cuadro)
        self.apellido.grid (row = 2, column = 1)
        #IngresarDNI
        Label(cuadro, text = 'DNI: ').grid(row = 3, column = 0)
        self.dni = Entry(cuadro)
        self.dni.grid(row = 3, column = 1)
        #IngresarLvlMembresía
        Label(cuadro, text = 'Nivel Membresía: ').grid(row = 4, column = 0)
        self.nivel = Entry(cuadro)
        self.nivel.grid(row = 4, column = 1)
        #BotónAgregarProducto
        self.principal.destroy()
        ttk.Button(cuadro, text = 'Agregar', command = self.agregarUsuario).grid(row = 5, columnspan = 2, sticky = W + E)
        

    def validarUsuario(self):
        return len(self.nombre.get()) and len(self.apellido.get()) != 0 and len(self.dni.get()) != 0 and len(self.nivel.get()) != 0 


    def eliminarUsuario(self):
        cuadro2 = LabelFrame(self.wind, text = 'Ingrese el DNI del usuario a eliminar: ')
        cuadro2.grid(row = 0, column = 0, columnspan = 3, pady = 40)
        #IngresarCodigo
        Label(cuadro2, text = 'DNI: ').grid(row = 1, column = 0)
        self.dni = Entry(cuadro2)
        self.dni.focus()
        self.dni.grid (row = 1, column = 1)
        self.principal.destroy()
       #BotónBorrarProducto
        ttk.Button(cuadro2, text = 'Borrar', command = self.borrarUsuario).grid(row = 5, columnspan = 4, sticky = W + E)


    def borrarUsuario(self):
        borrar = self.dni.get()
        query = f"DELETE FROM DatosClientes WHERE DNI = ?"
        self.consultar(query, [borrar])
        showinfo(title = "¡Genial!", message = "Cliente borrado exitosamente")


    def mostrarUsuario(self):
        cuadro3 = LabelFrame(self.wind, text = 'Clientes registrados: ')
        cuadro3.grid(row = 0, column = 0, columnspan = 3, pady = 40)
        self.wind.geometry("800x600")
        lista = ttk.Treeview(cuadro3, columns = (1, 2, 3), padding = "0", height = 8)

        lista.heading("#0", text="Nombres", anchor=CENTER)
        lista.heading("#1", text="Apellidos", anchor=CENTER)
        lista.heading("#2", text="DNI", anchor=CENTER)
        lista.heading("#3", text="Membresía", anchor=CENTER)

        lista.grid(row = 0, column = 0, columnspan = 3, pady = 40)

        elementos = self.retornoUsuario()

        for i in elementos:
            lista.insert("", 0, text=i[0], values=(i[1], i[2], i[3]))


    def retornoUsuario(self):
        pedir = "SELECT * FROM DatosClientes"
        filas = self.consultar(pedir)
        return filas


    def agregarUsuario(self):
        if self.validarUsuario():
            query = 'INSERT or IGNORE INTO DatosClientes VALUES(?, ?, ?, ?)'
            parametros = (self.nombre.get(), self.apellido.get(), self.dni.get(), self.nivel.get())
            self.consultar(query, parametros)
            showinfo(title = "¡Genial!", message = "Cliente añadido exitosamente")
        else:
            print("Los campos son requeridos.")


if __name__ == "__main__":
    app = Pedidos()
    app1 = Pedidos.ventanaPrincipal(app)