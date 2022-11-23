from Clase_Admin import *
from Clase_Clientes import *
from Funciones_DB import *
import sqlite3
import os
clear = lambda: os.system('cls')

class Log():
    
    db_nombre = "login.db"
    def Home(self):
        clear()
        print("HOME")
        print("1- LOGIN")
        print("2- SALIR")
        while True:
            user_option = input("Ingrese opcion: ")
            if user_option in ['1', '2']:
                break
        if user_option == '1':
            self.Login()
        else:
            clear()
            print("FIN")
            exit

    def Login(self):
        #coneccion con la base de datos
        db = sqlite3.connect('login.db')
        c = db.cursor()
        clear()
        print("     LOGIN BIBLIOTECA")
        user = input("Ingrese usuario: ")
        passw = input("Ingrese contraseña: ")

        c.execute('SELECT * FROM users WHERE user = ? AND password = ?', (user, passw))

        if c.fetchall():
            clear()
            c.execute('SELECT lvl FROM users WHERE user = ? AND password = ?', (user, passw))
            lvl = c.fetchall()

            print("Ingresando al sistema BIBLIOTECA...\n")
            if lvl == [(1,)]:
                print("Bienvenido Usuario")
                app = Pedidos()
                app.ventanaPrincipal()
            elif lvl == [(3,)]:
                print("Bienvenido Admin")
                app2 = Admin()
                app2.ventanaPrincipal()
            else:
                print("Algo salió mal")
                print(lvl)

        else:
            print("Usuario y/o contraseña incorrectos")

        c.close()

app3 = Log()
app3.Home()
