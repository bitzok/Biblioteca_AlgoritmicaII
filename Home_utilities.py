import Pedido
import Clase_Clientes
import Clase_Admin
import Funciones_DB

def verify_password(user,password):
    if password_exists(user,password):
        return True
    else:
        if password == "":
            print("ERROR, debe ingresar una contraseña")
        
        elif password_exists(user,password)==False:
            print("Contraseña incorrecta")
        return False

def validate_password(password):
    if password =="":
        print("ERROR, debe ingresar una contraseña")
    else:
        if len(password<3):
            print("ERROR, Contraseña muy corta")
        elif len (password>12):
            print("ERROR, contraseña muy larga")
    


def password_exists(user,password):
    if Funciones_DB.Funciones_Login_Db.password_exists(user,password):
        return True
    else:
        return False

def verify_user(user):
    if user_already_exists(user):
        return True
    else:
        if user == "":
            print("ERROR, debe ingresar un nombre de usuario")
        elif user_already_exists(user)==False:
            print(f"El usuario {user} no se encuentra registrado")
        return False
    
def user_already_exists(user):
    if Funciones_DB.Funciones_Login_Db.user_exists(user):
        return True
    else:
        return False

def new_user(user,passw,lvl):
    Funciones_DB.Funciones_Signin_Db.insert(user,passw,lvl)

def validate_level(user,passw):
    level=Funciones_DB.Funciones_Login_Db.level_exists(user,passw)
    if level:
        return level
    else:
        print("ERROR, nivel de usuario vacio")

def user_options():
    print("[1] PEDIR LIBRO ")
    print ("[2] +CLIENTES")
    option = input ("Ingrese una opcion: ")
    option = int(option)
    if (option == 1):
        app = Pedido.PedidoLibro()
        app.Llamada()
    elif (option == 2):
        app1= Clase_Clientes.Cliente()
        app1.Llamada()
    else:
        print("ERROR: Opcion invalida")
        user_options()

def admin_options():
    print("[1] PEDIR LIBRO ")
    print ("[2] +ADMIN")
    option = input ("Ingrese una opcion: ")
    option = int(option)
    if (option == 1):
        app = Pedido.PedidoLibro()
        app.Llamada()
    elif (option == 2):
        app2= Clase_Admin.Admin()
        app2.Llamada()
    else:
        print("ERROR: Opcion invalida")
        admin_options()
