import sqlite3
import os
clear = lambda: os.system('cls')

db_nombre = "login.db"

def Home():
    clear()
    print("HOME")
    print("1- SIGNUP")
    print("2- LOGIN")
    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        Signin()
    else:
        Login()

def Signin():
    clear()
    print("Registrar usuario")

def Login():
    #coneccion con la base de datos
    db = sqlite3.connect('login.db')
    c = db.cursor()
    print("     LOGIN BIBLIOTECA")
    user = input("Ingrese usuario: ")
    passw = input("Ingrese contraseña: ")

    c.execute('SELECT * FROM users WHERE user = ? AND password = ?', (user, passw))

    if c.fetchall():
        clear()
        c.execute('SELECT lvl FROM users WHERE user = ? AND password = ?', (user, passw))
        lvl = c.fetchall()

        print("Usuario correcto!")
        print("Ingresando al sistema")
        if lvl == [(1,)]:
            print("Bienvenido Usuario")
        elif lvl == [(3,)]:
            print("Bienvenido Admin")
        else:
            print("Algo salió mal")
            print(lvl)

    else:
        print("Ups, Usuario y/o contraseña incorrectos")

    c.close()

Home()
