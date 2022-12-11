import Clase_Clientes
import Clase_Admin 
from Funciones_DB import Funciones_Login_Db

def validate_password(password):
    if len(password) < 3 or len(password) > 12:
        print("La contraseña debe tener entre 3 y 12 caracteres")
        return False
    else:
        return True

def validate_user(user):
    length = False
    if len (user) >=1:
        length = True
    return length
    
def imput():
    print(">>>LOGIN<<<")
    attempts = 0
    while True:
        user = input("Ingrese el nombre de usuario: ")
        if validate_user(user):
            while True: 
                attempts += 1
                password = input("Ingrese contraseña : ")
                if validate_password(password):
                    print("Verificando...")
                    login(user,password)
                    break
                elif attempts >= 3:
                    password = None
                    print ("ERROR: DEMASIADOS INTENTOS")
                    break    
        else:
            if attempts >=3:
                print("ERROR: DEMASIADOS INTENTOS ")
            break
     
def login(user,passw):
        
        level=Funciones_Login_Db.user_exists(user,passw)
        if level:
            print("Login exitoso")
            print("Ingresando al sistema LIBRARY...\n")
            if level == [(1,)]:
                print("Bienvenido "+user+" :)")
                app = Clase_Clientes.Cliente()
                app.Llamada()
            elif level == [(3,)]:
                print("Bienvenido admin "+user)
                app2 = Clase_Admin.Admin()
                app2.Llamada()
            else:
                print("Algo salió mal")
        else:
            imput()