import sqlite3

db_nombre = "login.db"


def login():
    # connection to database
    db = sqlite3.connect('login.db')
    c = db.cursor()
    print("     LOGIN BIBLIOTECA")
    user = input("Ingrese usuario: ")
    passw = input("Ingrese contraseña: ")

    c.execute('SELECT * FROM users WHERE user = ? AND password = ?', (user, passw))

    if c.fetchall():
        c.execute(
            'SELECT lvl FROM users WHERE user = ? AND password = ?', (user, passw))
        lvl = c.fetchall()

        print("Usuario correcto!")
        print("Ingresando al sistema")
        if lvl == [(1,)]:
            print("Usuario")
        elif lvl == [(3,)]:
            print("Admin")
        else:
            print("Algo salió mal")
            print(lvl)

    else:
        print("Ups, El usuario o contraseña está incorrecto")

    c.close()

if __name__ == "__main__":
    login()
