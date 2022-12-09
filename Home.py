import sqlite3
import Clase_Clientes
import Clase_Admin

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
        access(option==1)
    cursor.close()

def register(user):
    validar(user)
    grant()

def validar(user):
    conn = sqlite3.connect('login.db')
    cursor =conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user =?',(user,)) 
    if cursor.fetchall():
        print("El nombre de usuario ya se encuentra registrado")
        access(option=2)
    else:
        while True:
            password = input("Ingrese contraseña: ")
            password1 = input ("Ingrese contraseña nuevamente: ")
            if (password == password1):
                print("Usuario registrado con exito")
                insert(user,password,1)
                break
            else:
                print("Contraseñas no coiciden")

def insert(user,password,lvl):
    conn = sqlite3.connect('login.db')
    cursor =conn.cursor()
    instruction=f"INSERT INTO users VALUES ('{user}','{password}','{lvl}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close() 

def access(option):
    global user
    if (option == 1):
        user = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese contraseña : ")
        login(user, password)
    elif (option ==2):
        print("Registrar")
        user = input("Ingrese nuevo usuario: ")
        register(user)

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