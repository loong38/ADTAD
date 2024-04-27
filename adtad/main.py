# 这是一个示例 Python 脚本。
import os.path
import subprocess
import sys

from adtad.CommandRuntime import CommandRuntime
from adtad.Config import Config
from adtad.argument_manage.Argumnet import Argument


class Main(object):
    def __init__(self):
        self.config = Config()
        self.setting_environment_variables()

    def setting_environment_variables(self):
        # 添加mysql环境变量
        MYSQL_HOME: str = self.config.get_mysql().get_mysql_path()
        os.environ["MYSQL_HOME"] = os.path.abspath(MYSQL_HOME)

        # 添加JAVA_HOME变量
        JAVA_HOME: str = self.config.get_java().get_java_path()
        os.environ["JAVA_HOME"] = os.path.abspath(JAVA_HOME)

        # 添加tomcat环境变量
        CATALINA_HOME: str = self.config.get_tomcat().get_tomcat_path()
        os.environ["CATALINA_HOME"] = os.path.abspath(CATALINA_HOME)

        path_variable = os.environ.get("PATH")
        os.environ[
            "PATH"] = f"{os.environ.get('MYSQL_HOME')}{os.sep}bin;{os.environ.get('JAVA_HOME')}{os.sep}bin;{os.environ.get('CATALINA_HOME')};{path_variable}"
        pass


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 切换根目录未上一级
    # os.chdir("../")
    Main()
    Argument(sys.argv[1:])
    # c = CommandRuntime()
    # c.execute(['mysqld',"--initialize-insecure"])
    pass

    # runtime = CommandRuntime("dira")
    # runtime.execute()
    # print(runtime.execute().stderr)
