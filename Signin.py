from Login import validate_password,validate_user
from Funciones_DB import Funciones_Signin_Db

def signin():
    print(">>>SIGNIN<<")
    attempts = 0
    while True:
        user = input("Ingrese el nombre de usuario: ")
        if validate_user(user):
            buscar = Funciones_Signin_Db.search(user)
            if buscar: 
                while True:
                    password = input("Ingrese contraseña: ")
                    attempts += 1
                    if validate_password(password):
                        print("Verificando...")
                        password1 = input("Ingrese contraseña nuevamente: ")
                        if (password == password1):
                            insertar=Funciones_Signin_Db.insert(user, password,1)
                            print("Nuevo usuario registrado!... ")
                            insertar
                            break
                        else:
                            print("Contraseñas no coinciden ")
                    elif attempts >= 3:
                        password = None
                        print("ERROR: DEMASIADOS INTENTOS")
                        break
            else:
                print("El usuario ya se encuentra registrado")
        else:
            attempts+=1
            print("Intente nuevamente")
            if attempts >= 3:
                print("ERROR: DEMASIADOS INTENTOS")
                break
    
