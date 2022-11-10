from tkinter import *
from tkinter.messagebox import *

import sqlite3

import Libros as Lib

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

def login():
    #connection to database
    db=sqlite3.connect('login.db')
    c = db.cursor()

    user = username.get()
    passw = password.get()
    
    c.execute('SELECT * FROM users WHERE user = ? AND password = ?', (user, passw))

    if c.fetchall():
        showinfo(title = "Usuario correcto!", message = "Ingresando al sistema")
        screen_login.destroy()
        app = Lib.Admin()
        app1 = Lib.Admin.ventanaPrincipal(app)
        
    else:
        showerror(title = "Ups", message = "El usuario o contraseña está incorrecto")

    c.close()

if __name__ == "__main__":
    root()
    