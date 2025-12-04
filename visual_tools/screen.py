import os
import sys

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def clear_line(line: int):
    print_at(0, line, " " * 100)

def print_at(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y + 1, x + 1, text))
     sys.stdout.flush()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored(s: any, color: str) -> str:
    return f"{color}{s}{bcolors.ENDC}"


class ColorAlternator:
    def __init__(self):
        self.colors = [bcolors.OKGREEN, bcolors.RED, bcolors.OKBLUE, bcolors.WARNING]
    
    def next(self, s: any) -> str:
        c = self.colors.pop(0)
        self.colors.append(c)
        return colored(s, c)
