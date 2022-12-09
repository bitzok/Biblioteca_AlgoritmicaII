import sqlite3
from os import system
from Login import validate_password,validate_user,search

def signin():
    print(">>>SIGNIN<<")
    attempts = 0
    while True:
        user = input("Ingrese el nombre de usuario: ")
        if (search(user) == False and validate_user(user) == True):
            while True:
                password = input("Ingrese contraseña: ")
                attempts += 1
                if validate_password(password):
                    print("Verificando...")
                    password1 = input("Ingrese contraseña nuevamente: ")
                    if (password == password1):
                        print("Nuevo usuario registrado!... ")
                        insert(user, password, 1)
                        system("cls")
                        break
                    else:
                        print("Contraseñas no coinciden ")
                elif attempts >= 3:
                    password = None
                    system("cls")
                    print("ERROR: DEMASIADOS INTENTOS")
                    break
        else:
            attempts+=1
            print("Intente nuevamente")
            if attempts >= 3:
                system("cls")
                print("ERROR: DEMASIADOS INTENTOS")
                break
    
def insert(user, password, lvl):
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()
    instruction = f"INSERT INTO users VALUES ('{user}','{password}','{lvl}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
