from adtad.argument_manage.Initialize import Initialize


class Argument(object):
    def __init__(self, argv):
        if "initialize" in argv[0]:
            Initialize(argv[1:])
            return
        # TODO 其他参数
        pass
