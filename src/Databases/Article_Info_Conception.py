import mysql.connector as mysql
import json

#ams_db = mysql.connect(host="localhost", user="root", password="", database="AMS")
ams_db = mysql.connect(host="%manuelfreistein", user="ManuelFreistein", password="AMS", database="AMS")
command_handler = ams_db.cursor(buffered=True)

def get_all_article_suggestions() -> list:
    command_handler.execute("SELECT * FROM article_info_conception")
    return command_handler.fetchall()

def get_article_assessments(article_id: int) -> list:
    command_handler.execute("SELECT assessments FROM article_info_conception WHERE id = %s", (article_id,))
    return command_handler.fetchall()

def set_article_assessments(assessments: json, article_id: int):
    command_handler.execute("UPDATE article_info_conception SET assessments = %s WHERE id = %s",
                            (assessments, article_id))
    ams_db.commit()

def get_article_suggestion_comments(article_id) -> list:
    command_handler.execute("SELECT comments FROM article_info_conception WHERE id = %s", (article_id,))
    return command_handler.fetchall()

def add_article_suggestion_comment(comments: json, article_id: int):
    command_handler.execute("UPDATE article_info_conception SET comments = %s WHERE id = %s", (comments, article_id))
    ams_db.commit()

def add_article_suggestion(article_suggestion_info: tuple):
    command_handler.execute("INSERT INTO article_info_conception "
                            "(title, outline, wordcount,"
                            "suggested_author, suggested_assignee, suggested_reviewer,"
                            "creator, date_created, date_last_updated, assessments, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            article_suggestion_info)
    ams_db.commit()
