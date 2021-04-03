from tkinter import *
import hashlib
import csv


def register():
    username = register_username.get()
    password = register_password.get()
    hashed_password = hashlib.sha256(str.encode(password)).hexdigest()
    info = [username, hashed_password]

    if len(username) == 0 or len(password) == 0:
        pass
    else:
        with open("storage.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(info)
        print("USERNAME AND PASSWORD CREATED SUCCESSFULLY")
        register_entry1.delete(0, END)
        register_entry2.delete(0, END)
        file.close()


def login():
    username = login_username.get()
    password = login_password.get()
    hashed_password = hashlib.sha256(str.encode(password)).hexdigest()
    info = [username, hashed_password]

    if len(username) == 0 or len(password) == 0:
        pass
    else:
        with open("storage.csv", "r", newline='') as file:
            reader = csv.reader(file)
            users = []
            for row in reader:
                users.append(row)
            if info in users:
                print("LOGGED IN SUCCESSFULLY")
            else:
                print("FAILED TO LOGIN")
        login_entry1.delete(0, END)
        login_entry2.delete(0, END)
        file.close()


def register_window():
    global register_screen
    register_screen = Toplevel(welcome_screen)
    register_screen.title("Register Page")
    register_screen.geometry("300x250")
    Label(register_screen, text="").pack()
    Label(register_screen, text="Register Here").pack()
    Label(register_screen, text="").pack()

    global register_username
    global register_password
    register_username = StringVar()
    register_password = StringVar()
    global register_entry1
    global register_entry2

    Label(register_screen, text="Username").pack()
    register_entry1 = Entry(register_screen, textvariable=register_username)
    register_entry1.pack()
    Label(register_screen, text="Password").pack()
    register_entry2 = Entry(register_screen, textvariable=register_password)
    register_entry2.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command=register).pack()


def login_window():
    global login_screen
    login_screen = Toplevel(welcome_screen)
    login_screen.title("Login Page")
    login_screen.geometry("300x250")
    Label(login_screen, text="").pack()
    Label(login_screen, text="Login Here").pack()
    Label(login_screen, text="").pack()

    global login_username
    global login_password
    login_username = StringVar()
    login_password = StringVar()
    global login_entry1
    global login_entry2

    Label(login_screen, text="Username").pack()
    login_entry1 = Entry(login_screen, textvariable=login_username)
    login_entry1.pack()
    Label(login_screen, text="Password ").pack()
    login_entry2 = Entry(login_screen, textvariable=login_password)
    login_entry2.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login).pack()


def welcome_window():
    global welcome_screen
    welcome_screen = Tk()
    welcome_screen.geometry("400x200")
    welcome_screen.title("Password Hasher Tester")
    Label(text="Welcome! You can either login or register.", bg="grey", width="300", height="2", font='Helvetica').pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login_window).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register_window).pack()

    welcome_screen.mainloop()


welcome_window()
