from Home_utilities import*
from CreatePassword import create_password
from CreateUser import create_user
def signin():
    print("\t>>>SIGNIN<<")
    while True:
        user = input("Ingrese el nombre de usuario: ")
        if user_already_exists(user)==False:
            u =create_user(user)
            if u.validate_user():
                password = input('Insert Password: ')
                password2 = input('Repeat Password: ')
                passw = create_password(password)
                if passw.validate():
                    if passw.compare(password2) is True:
                        print('Usuario Registrado con exito')
                        new_user(user,password,1)
                    else:
                        print ("ERROR,Contraseñas no coiciden")
                    break
                else:
                    print(passw.validate())
            else:
                print(u.validate_user())   
        else:
            print("El usuario ya se encuentra registrado")
        break
