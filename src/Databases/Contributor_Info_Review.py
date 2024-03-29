"""
Acts as connection to Database AMS/contributor_info_review
"""

from mysql import connector as mysql

ams_db = mysql.connect(host="localhost", user="root", password="", database="AMS")
command_handler = ams_db.cursor(buffered=True)


def get_all_contributors() -> list:
    """
    :return:
    """
    command_handler.execute("SELECT * FROM contributor_info_review")
    return command_handler.fetchall()


def get_contributor_info_from_id(contributor_id: int) -> list:
    """
    :param contributor_id:
    :return:
    """
    command_handler.execute("SELECT * FROM contributor_info_review WHERE id = %s", (contributor_id,))
    return command_handler.fetchall()


def get_id_from_last_name(requested_last_name: str) -> list:
    """
    :param requested_last_name:
    :return:
    """
    command_handler.execute("SELECT id FROM contributor_info_review WHERE last_name = %s", (requested_last_name,))
    return command_handler.fetchall()
