from adtad.CommandRuntime import CommandRuntime
from adtad.argument_manage.InitializeMysqlArgument import InitializeMysqlArgument


class TomcatHandler(object):
    def __init__(self, initial: InitializeMysqlArgument):
        self.command = []
        self.initial: InitializeMysqlArgument = initial

    def initialize(self):
        pass
    # TODO initial
    # self.command = ["mysqld", "--initialize-insecure"]
    # if self.initial.get_no_data():
    #     # self.command.append("--no-data")
    #     pass
    # if self.initial.get_no_default_account():
    #     pass
    # pass

    def start(self):
        self.command = [config.get_tomcat(), "start", "mysql"]
        pass

    def stop(self):
        self.command = ["net", "stop", "mysql"]
        pass

    def run(self):
        runtime = CommandRuntime(self.command)
        runtime.execute()
