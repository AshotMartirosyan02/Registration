import data_base
from face_registracion import face_id
from pwinput import pwinput


def valid_input(prompt, func, *args):
    if func == valid_password or func == repeat_password:
        user_input = pwinput(prompt)
        while not func(user_input, *args):
            print("Input failed, please try again.")
            user_input = pwinput(prompt)
        return user_input
    else:
        user_input = input(prompt)
        while not func(user_input, *args):
            print("Input failed, please try again.")
            user_input = input(prompt)
        return user_input


def valid_username(username):
    return 5 <= len(username) <= 20 and username.isalnum()


def valid_password(password):
    return (len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(
        c.islower() for c in password))


def repeat_password(password, rep_password):
    return password == rep_password


def register_user():
    data_base.create_database()
    username = valid_input("Enter username:  ", valid_username)
    password = valid_input("Enter password:  ", valid_password)
    repeat = valid_input("Repeat Passord:  ", repeat_password, password)

    print("Create your Face_id:")
    image_address = face_id(username)
    data_base.add_new_user(username, password, image_address)
    print("User successfully registered.")
