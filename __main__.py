from tkinter import *
from tkinter.messagebox import *
from Funciones_DB import *

import sqlite3

import Clase_Admin as Lib
import Clase_Clientes as Cli

db_nombre = "login.db"

def root():
    global screen_login
    global username
    global password
    screen_login = Tk()
    screen_login.title("INGRESAR USUARIO")
    screen_login.geometry("350x150+500+250")

    Label(screen_login, text = "Usuario").pack()
    username = Entry(screen_login, font="Ubuntu 12", justify="center")
    username.pack()

    Label(screen_login, text = "Contraseña").pack()
    password = Entry(screen_login, show = "*", font="Ubuntu 12", justify="center")
    password.pack()

    enter = Button(text ="Login", font = "Ubuntu 14", command = login)
    enter.config(activebackground = "dark blue")
    enter.pack()

    screen_login.mainloop()

def consultar(query, parameters = ()):
    with sql.connect(db_nombre) as conn:
        cursor = conn.cursor()
        cursor.execute(query, parameters) 
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

def login():
    #connection to database
    db=sqlite3.connect('login.db')
    c = db.cursor()

    user = username.get()
    passw = password.get()

    conn  = sql.connect(db_nombre)
    cursor = conn.cursor()
    cursor.execute('SELECT lvl FROM users WHERE user = ? AND password = ?', (user, passw))
    lvl = cursor.fetchall()


    c.execute('SELECT * FROM users WHERE user = ? AND password = ?', (user, passw))

    if c.fetchall():
        showinfo(title = "Usuario correcto!", message = "Ingresando al sistema")
        screen_login.destroy()

        if lvl == [(1,)]:
            app = Cli.Pedidos()
            app1 = Cli.Pedidos.ventanaPrincipal(app)
        elif lvl == [(3,)]:
            app = Lib.Admin()
            app1 = Lib.Admin.ventanaPrincipal(app)
        else: 
            print("Algo salió mal")
            print(lvl)
        
    else:
        showerror(title = "Ups", message = "El usuario o contraseña está incorrecto")

    c.close()




    
if __name__ == "__main__":
    root()