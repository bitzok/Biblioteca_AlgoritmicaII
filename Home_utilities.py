import Pedido
import Clase_Clientes
import Clase_Admin

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
        user_options()