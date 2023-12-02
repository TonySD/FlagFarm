import sys
from colorama import init, Fore, Style
from config import *

init(autoreset=True)
'''
0 - Trace
1 - Debug
2 - Info
3 - Error
4 - Fatal
5 - None
'''
class Logger:
    def __init__(self, tag: str = "Undefined", error_level: int = LOG_LEVEL):
        self.tag = tag
        self.error_level = error_level
        

    def trace(self, *args):
        if self.error_level > 0: return
        arguments = ' '.join(map(str, args))
        message = f"[TRACE : {self.tag}] {arguments}"

        self.write_to_log(message)
        print(Fore.LIGHTMAGENTA_EX + message)

    def debug(self, *args):
        if self.error_level > 1: return
        arguments = ' '.join(map(str, args))
        message = f"[DEBUG : {self.tag}] {arguments}"

        self.write_to_log(message)
        print(Fore.GREEN + message)

    def info(self, *args):
        if self.error_level > 2: return
        arguments = ' '.join(map(str, args))
        message = f"[INFO  : {self.tag}] {arguments}"

        self.write_to_log(message)
        print(Fore.BLUE + message)

    def error(self, *args):
        if self.error_level > 3: return
        arguments = ' '.join(map(str, args))
        message = f"[ERROR : {self.tag}] {arguments}"

        self.write_to_log(message)
        print(Fore.RED + message)

    def fatal(self, *args):
        if self.error_level > 4: return
        arguments = ' '.join(map(str, args))
        message = f"[FATAL : {self.tag}] {arguments}"

        self.write_to_log(message)
        print(Fore.LIGHTRED_EX + Style.BRIGHT + message)
        sys.exit(1)

    def write_to_log(self, message):
        if LOG_FILENAME:
            with open(LOG_FILENAME, "a+") as file:
                file.write(message + '\n')