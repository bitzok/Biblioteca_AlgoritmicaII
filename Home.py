import sqlite3
from Clase_Clientes import Pedidos

granted = False
def grant():
    global granted
    granted = True

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
            if level == [(1,)]:
                print("Bienvenido Usuario")
                app = Pedidos()
                app.ventanaPrincipal()
            elif level == [(3,)]:
                print("Bienvenido Admin")
<<<<<<< HEAD
                app2 = Admin()
                app2.ventanaPrincipal()
=======
                app2 = Clase_Admin.Admin()
                app2.Llamada()
>>>>>>> 49449e562ad4218b432ae9f8a1de08155e4aa1b9
            else:
                print("Algo salió mal")
    else:
        print("Usuario y/o contraseña incorrectos")
    cursor.close()

def register(user, password):
    grant()

def access(option):
    global user
    if (option == 1):
        user = input("Ingrese el nombre de usuario: ")
        password = input("Enter your password: ")
        login(user, password)
    else:
        print("Ingrese un nombre de usuario y contraseña")
        user = input("Ingrese nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        register(user, password)

def home():
    global option
    print("Bienvenido a Library *******")
    print("Ingrese una opcion\n[1]Login\n[2]Register")
    option = input("Opcion: ")
    option=int(option)
    if (option != 1 and option != 2):
        home()
    else:
        begin()

def begin():
    access(option)
    if (granted):
        print("Bienvenido a Library")
        print("### USER DETAILS ###")
        print("Username: ", user)