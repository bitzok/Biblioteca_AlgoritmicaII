from Login import imput
from Signin import signin
from os import system

def home():
    global option
    print(">>>BIENVENIDO<<<")
    while True:
        print("Ingrese una opcion:\n[1]Login\n[2]Register")
        option = input("Opcion: ")
        option=int(option)
        system("cls")
        if (option == 1):
           imput()     
        elif (option ==2):
            signin()
        else:
            print(">>>Opcion invalida<<<")
