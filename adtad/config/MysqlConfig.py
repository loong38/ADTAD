import os
import sys


class MysqlConfig:

    def __init__(self, mysql_path: str, mysql_user: str, mysql_password: str, mysql_db: str, sql_file: str = None):
        mysql_bin = f"{os.path.abspath(mysql_path)}{os.sep}bin{os.sep}mysql.exe"

        if not os.path.exists(mysql_bin):
            sys.exit("Cannot find mysql.exe,Check whether the path is correct")

        self.__config = {"path": mysql_path, "account": mysql_user, "password": mysql_password, "mysql_db": mysql_db}

    def get_mysql_path(self):
        return self.__config["path"]

    def get_mysql_user(self):
        return self.__config["account"]

    def get_mysql_password(self):
        return self.__config["password"]

    def get_mysql_db(self):
        return self.__config["mysql_db"]
