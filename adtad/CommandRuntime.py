import os
import subprocess


class CommandRuntime(object):
    def __init__(self, *command):
        self.__command = list(command)[0]
        print(self.__command)

    def execute(self):
        result = subprocess.run(self.__command, shell=True, env=os.environ, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
