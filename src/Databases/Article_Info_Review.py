import mysql.connector as mysql

ams_db = mysql.connect(host="127.0.0.1", user="root", password="", database="AMS")
command_handler = ams_db.cursor(buffered=True)

def get_all_articles_in_review() -> list:
    command_handler.execute("SELECT * FROM article_info_review")
    return command_handler.fetchall()
