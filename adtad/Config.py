import configparser
import os.path


class ConfigMysql:
    def __init__(self, mysql_path: str, mysql_user: str, mysql_password: str, mysql_db: str):
        self.__mysql_db = mysql_db
        self.__mysql_password = mysql_password
        self.__mysql_user = mysql_user
        self.__mysql_path = mysql_path

    def get_mysql_path(self):
        return self.__mysql_path

    def get_mysql_user(self):
        return self.__mysql_user

    def get_mysql_password(self):
        return self.__mysql_password

    def get_mysql_db(self):
        return self.__mysql_db


class Tomcat:
    def __init__(self, tomcat_path: str):
        self.__tomcat_path = tomcat_path

    def get_tomcat_path(self):
        return self.__tomcat_path


class Java:
    def __init__(self, java_path: str):
        self.__java_path = java_path

    def get_java_path(self):
        return self.__java_path


class Config:
    __initialize_data = '''
[mysql]
mysql_path="./mysql"
username="root"
password="root"
database="mysql"
#sql_file=""

[tomcat]
tomcatDir="./apache"

[java]
install_path="./jdk"
'''

    def __init__(self):
        self.__config_path = "./config/config.ini"
        self.__config = configparser.ConfigParser()

        if not os.path.exists(self.__config_path):
            self.create_config_file()
        Config.initialize_data = None

        config = configparser.ConfigParser()
        config.read(self.__config_path)

        self.__mysql = ConfigMysql(config['mysql']['path'],
                                   config['mysql']['user'],
                                   config['mysql']['password'],
                                   config['mysql']['database'])
        # self.__sql_file = config['mysql']['sql_file']

        self.__java = Java(config['java']['path'])

        self.__tomcat = Tomcat(config['tomcat']['path'])
        pass

    def create_config_file(self):
        with open(self.__config_path, 'w') as configfile:
            configfile.write(Config.__initialize_data)
        pass

    def get_mysql(self):
        return self.__mysql

    def get_java(self):
        return self.__java

    def get_tomcat(self):
        return self.__tomcat