import mysql.connector as mysql

#ams_db = mysql.connect(host="localhost", user="root", password="", database="AMS")
ams_db = mysql.connect(host="manuelfreistein", user="ManuelFreistein", password="AMS", database="AMS")
command_handler = ams_db.cursor(buffered=True)

def get_all_contributors() -> list:
    command_handler.execute("SELECT * FROM contributor_info_review")
    return command_handler.fetchall()

def get_contributor_info_from_id(contributor_id: int) -> list:
    command_handler.execute("SELECT * FROM contributor_info_review WHERE id = %s", (contributor_id,))
    return command_handler.fetchall()

def get_id_from_last_name(requested_last_name: str) -> list:
    command_handler.execute("SELECT id FROM contributor_info_review WHERE last_name = %s", (requested_last_name,))
    return command_handler.fetchall()
