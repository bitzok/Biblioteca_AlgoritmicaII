from Login import imput
from Signin import signin

def home():
    print(">>>BIENVENIDO<<<")
    while True:
        option = None
        print("Ingrese una opcion:\n[1]Login\n[2]Register")
        option = input("->Opcion: ")
        if option is not None:
            if int(option) == 1:
                imput()     
            elif int (option) ==2:
                signin()
            else:
                print(f"Opcion {option} invalida")
        else:
            print ("ERROR, debe ingresar una opcion")
            

        
