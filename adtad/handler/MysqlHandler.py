from adtad.CommandRuntime import CommandRuntime
from adtad.argument_manage.InitializeMysqlArgumnet import InitializeMysqlArgumnet


class MysqlHandler(object):
    def __init__(self, initial: InitializeMysqlArgumnet):
        self.command = []
        self.initial: InitializeMysqlArgumnet = initial

    def initialize(self):
        # TODO initial
        self.command = ["mysqld", "--initialize-insecure"]
        if self.initial.get_no_data():
            # self.command.append("--no-data")
            pass
        if self.initial.get_no_default_account():
            pass
        pass

    def start(self):
        self.command = ["net", "start", "mysql"]
        pass

    def stop(self):
        self.command = ["net", "stop", "mysql"]
        pass

    def remove_service(self):
        self.command = ["mysqld", "-remove"]
        pass

    def add_service(self):
        self.command = ["mysqld", "-install"]
        pass

    def run(self):
        runtime = CommandRuntime(self.command)
        runtime.execute()
