import getopt


def show_help():
    print('ADTAD command line tool menu')
    print('')
    print('Options:')
    print('  -h | --help                Display this help message and exit')
    print('  --noDefaultData            no import default android data')
    print('  --noDefaultAccount         no import default user "user"@"%" password "user"')
    print('')


class InitializeMysqlArgumnet(object):
    def __init__(self, argv: list):
        self.short_opts: str = "h"
        self.long_opts: list = ['help', 'noData', 'noDefaultAccount']
        self.noData:bool = False
        self.noDefaultAccount:bool = False
        print(argv)
        try:
            opts, args = getopt.getopt(argv, self.short_opts, self.long_opts)
        except getopt.GetoptError as err:
            print(err)
            # print("No initialize arguments given")
            print("Usage: -h --help")
            return

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                show_help()
            elif opt in "--noData":
                self.noData: bool = True
            elif opt in "--noDefaultAccount":
                self.noDefaultAccount: bool = True
            else:
                print(f"opt {opt} not recognized")

    def get_no_data(self):
        return self.noData

    def get_no_default_account(self):
        return self.noDefaultAccount
