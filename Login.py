from Home_utilities import*

def imput():
    print("\t>>>LOGIN<<<")
    while True:
        user = input("Ingrese el nombre de usuario: ")
        if verify_user(user):
            password = input("Ingrese contraseña : ")
            if verify_password(user,password):
                print("Verificando...")
                login(user,password)
                break
            else:
                print("Volviendo al menu principal")
                break
        break            
     
def login(user,passw):
        level=validate_level(user,passw)
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
                print("ERROR: nivel invalido")
                print("No se puede iniciar sesion")
        else:
            imput() 