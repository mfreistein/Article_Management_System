import mysql.connector as mysql

ams_db = mysql.connect(host="localhost", user="root", password="ams", database="AMS")
command_handler = ams_db.cursor(buffered=True)

def get_all_articles_in_review() -> list:
    command_handler.execute("SELECT * FROM article_info_review")
    return command_handler.fetchall()
