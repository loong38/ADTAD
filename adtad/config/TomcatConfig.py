class TomcatConfig:
    def __init__(self, tomcat_path: str):
        self.__tomcat_path = tomcat_path

    def get_tomcat_path(self):
        return self.__tomcat_path
