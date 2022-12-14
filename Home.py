from Login import imput
from Signin import signin

def home():
    print(">>>BIENVENIDO<<<")
    while True:
        print("Ingrese una opcion:\n[1]Login\n[2]Register")
        option = input("Opcion: ")
        option=int(option)
        if (option == 1):
           imput()     
        elif (option ==2):
            signin()
        else:
            print(">>>Opcion invalida<<<")
