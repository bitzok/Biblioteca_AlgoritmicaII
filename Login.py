from Home_utilities import*
import Funciones_DB
    
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
            break
     
def login(user,passw):
        level=Funciones_DB.Funciones_Login_Db.user_exists(user,passw)
        if level:
            print("Login exitoso")
            print("Ingresando al sistema LIBRARY...\n")
            if level == [(1,)]:
                print("Bienvenido "+user+" :)")
                user_options()
            elif level == [(3,)]:
                print("Bienvenido admin "+user)
                admin_options()
            else:
                print("Algo salió mal")
        else:
            imput()