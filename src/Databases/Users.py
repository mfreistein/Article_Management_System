import mysql.connector as mysql

#ams_db = mysql.connect(host="localhost", user="root", password="", database="AMS")
ams_db = mysql.connect(host="%manuelfreistein", user="ManuelFreistein", password="AMS", database="AMS")

command_handler = ams_db.cursor(buffered=True)

def get_all_users() -> list:
    command_handler.execute("SELECT * FROM users")
    return command_handler.fetchall()

def get_user_info_from_id(user_id: int):
    command_handler.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    return command_handler.fetchall()