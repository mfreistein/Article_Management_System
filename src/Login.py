"""
Opens the Login Page and verifies the username and password
"""
from Databases import Users #pylint: disable=import-error
from Conception import View, Model, Controller #pylint: disable=import-error

#pylint: disable=line-too-long
#pylint: disable=invalid-name


def login_page():
    """
    Prompts users to type in username and password
    """
    while 1:
        print("")
        print("Welcome to the Article Management System")
        print("")
        print("To login please type in your username and password")
        print("")
        username = input(str("Username: "))
        password = input(str("Password: "))
        user_id = verify_username_password(username, password)
        if user_id == -1:
            print("")
            print("Wrong username or password. Please try again.")
        else:
            model = Model.Model()
            view = View.View()
            Controller.Controller(model, view, user_id)


def verify_username_password(username: str, password: str) -> int:
    """checks if there is a user in the AMS database 'users'
    with the input 'username' and 'password'.
    returns the user's 'id' if true and None if false"""
    Users.command_handler.execute\
        ("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = Users.command_handler.fetchall()
    if user:
        user_id = user[0][0]
        return user_id
    return -1
