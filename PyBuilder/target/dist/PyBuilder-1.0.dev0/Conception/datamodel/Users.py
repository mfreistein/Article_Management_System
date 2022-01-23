class User:

    def __init__(self, username, password, name, email, privilege):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__email = email
        self.__privilege = privilege
        self.__id = self.set_id()

    def add_to_sql_db_users(self) -> int:
        """Adds user to SQL 'users' database.
        The SQL database assigns an id.
        Returns SQL database id as int"""