import configparser
import os.path
import sys

from adtad.config.JavaConfig import JavaConfig
from adtad.config.MysqlConfig import MysqlConfig
from adtad.config.TomcatConfig import TomcatConfig


class Config:

    def create_config_file(self):
        config_path = self.__config_path
        if not os.path.isdir(os.path.dirname(config_path)):
            os.mkdir(os.path.dirname(config_path))

        if not os.path.isfile(config_path):
            initialize_data = \
                '''
[mysql]
path=mysql
account=root
password=root
database=mysql
#sql_file=

[tomcat]
path=apache

[java]
path=jdk
'''
            with open(self.__config_path, 'w') as configfile:
                configfile.write(initialize_data)
                configfile.close()

    def __init__(self):
        self.__config_path = "./config.ini"
        self.__config = configparser.ConfigParser()

        self.create_config_file()

        config = configparser.ConfigParser()
        config.read(self.__config_path)

        self.__mysql = MysqlConfig(config['mysql']['path'],
                                   config['mysql']['account'],
                                   config['mysql']['password'],
                                   config['mysql']['database'])
        # self.__sql_file = config['mysql']['sql_file']

        self.__java = JavaConfig(config['java']['path'])

        self.__tomcat = TomcatConfig(config['tomcat']['path'])

        pass

    def get_mysql(self):
        return self.__mysql

    def get_java(self):
        return self.__java

    def get_tomcat(self):
        return self.__tomcat
