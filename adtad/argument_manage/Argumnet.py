import getopt
import sys

from adtad.CommandRuntime import CommandRuntime
from adtad.argument_manage.InitializeMysqlArgumnet import InitializeMysqlArgumnet
from adtad.handler.MysqlHandler import MysqlHandler


class Argument(object):
    def __init__(self, argv):
        # 定义命令行参数
        self.short_opts = 'h'
        self.long_opts = ['help', 'initialize', 'uninstall', "start", "console", "stop"]
        # --console
        # TODO ERROR IndexError: list index out of range
        if not argv:
            self.show_help()
            sys.exit(0)

        if "initialize" in argv[0]:
            initializeMysqlArgv = InitializeMysqlArgumnet(argv[1:])
            mysqlHandler = MysqlHandler(initializeMysqlArgv)
            mysqlHandler.initialize()
            mysqlHandler.run()
            # mysqlHandler
            return

        opts, args = getopt.getopt(argv, self.short_opts, self.long_opts)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.show_help()
                sys.exit(0)
            elif opt in "--console":
                runtime = CommandRuntime(["cmd", "/c", "start", "cmd", "/k"])
                runtime.execute()
            else:
                print(f"opt {opt} not recognized")
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
