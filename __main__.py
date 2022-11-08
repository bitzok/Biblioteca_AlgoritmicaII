from tkinter import *
from tkinter.messagebox import *

import sqlite3

from Codigo1 import * 

def root():
    global screen_login
    global username
    global password
    screen_login = Tk()
    screen_login.title("LOGIN LIBRARY")
    screen_login.geometry("350x150+500+250")

    Label(screen_login, text = "User").pack()
    username = Entry(screen_login, font="Ubuntu 12", justify="center")
    username.pack()

    Label(screen_login, text = "Password").pack()
    password = Entry(screen_login, show = "*", font="Ubuntu 12", justify="center")
    password.pack()

    enter = Button(text ="Login", font = "Ubuntu 14", command = login)
    enter.config(activebackground = "dark blue")
    enter.pack()

    screen_login.mainloop()

def login():
    #connection to database
    db=sqlite3.connect('login.db')
    c = db.cursor()

    user = username.get()
    passw = password.get()
    
    c.execute('SELECT * FROM users WHERE user = ? AND password = ?', (user, passw))

    if c.fetchall():
        showinfo(title = "Successful Login", message = "Successfully logged in session")
        window = Tk()
        app = Admin(window)
        app1 = Admin.editarStock(app)
        window.mainloop()

    else:
        showerror(title = "Something go wrong", message = "Wrong username or password")
        option = askretrycancel (title = "Try Again", message ="Want to try again ? ")
        print(option)
        if option == True:
            showinfo(title = "New try", message = "Enter the data correctly")
        else:
            screen_login.destroy()

    c.close()

if __name__ == "__main__":
    root()
    