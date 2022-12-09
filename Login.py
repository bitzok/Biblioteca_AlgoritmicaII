import sqlite3
from os import system
import Clase_Clientes
import Clase_Admin 


def validate_password(password):
    if len(password) < 3 or len(password) > 12:
        print("La contraseña debe tener entre 3 y 12 caracteres")
    else:
        print ("Datos validos")
        return True
    return False

def validate_user(user):
    length = False
    if len (user) >=4:
        length = True
    if length:
        print ("Usuario valido")
        return True
    else:
        system("cls")
        print("Usuario invalido")  
        return False
    
def search(user):
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user =?', (user,))
    if cursor.fetchall():
        return True
    else:
        return False

def imput():
    print(">>>LOGIN<<<")
    attempts = 0
    while True:
        user = input("Ingrese el nombre de usuario: ")
        if (search(user) == True and validate_user(user) == True):
            while True: 
                password = input("Ingrese contraseña : ")
                attempts += 1
                if validate_password(password):
                    print("Verificando...")
                    login(user,password)
                    break
                elif attempts >= 3:
                    password = None
                    system("cls")
                    print ("ERROR: DEMASIADOS INTENTOS")
                    break
        else:
            attempts+=1
            if attempts >= 3:
                system("cls")
                print("ERROR: DEMASIADOS INTENTOS")
                break
     
def login(user, passw):
    success = False
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user = ? AND password = ?', (user, passw))
    if cursor.fetchall():
        cursor.execute('SELECT lvl FROM users WHERE user = ? AND password = ?', (user, passw))
        level = cursor.fetchall()
        success=True
        if(success):
            print("Login exitoso")
            print("Ingresando al sistema LIBRARY...\n")
            system("cls")
            if level == [(1,)]:
                print("Bienvenido Usuario")
                app = Clase_Clientes.Cliente()
                app.Llamada()
            elif level == [(3,)]:
                print("Bienvenido Admin")
                app2 = Clase_Admin.Admin()
                app2.Llamada()
            else:
                print("Algo salió mal")
    else:
        print("Usuario y/o contraseña incorrectos")
        imput()
    cursor.close()