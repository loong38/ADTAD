import getopt

from adtad.argument_manage.InitializeMysql import InitializeMysql
from adtad.handler.MysqlHandler import MysqlHandler


class Argument(object):
    def __init__(self, argv):
        # 定义命令行参数
        self.short_opts = 'h'
        self.long_opts = ['help', 'initialize', 'uninstall', "start", "console", "stop", "noImportData"]

        # TODO ERROR IndexError: list index out of range
        if "initialize" in argv[0]:
            initial = InitializeMysql(argv[1:])
            mysqlHandler = MysqlHandler(initial)
            return
        opts, args = getopt.getopt(argv[1:], self.short_opts, self.long_opts)
        # if opts
        pass

    # 显示帮助信息
    def show_help(self):
        print('')
        print('Options:')
        print('  -h | --help       Display this help message and exit')
        print('  --initialize      initialize mysql service and import data')
        print('  --uninstall       remove mysql service')
        print('  --start           start mysql service and tomcat service')
        print('  --stop            stop mysql service and tomcat service')
        print('  --console         open cmd in current environment')
        print('')
