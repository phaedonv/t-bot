import sys
import time

from colorama import Fore
from termcolor import colored

def countdown(sec):
    for remaining in range(sec, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(Fore.LIGHTMAGENTA_EX + "{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write(Fore.GREEN + "\rComplete!            \n")

countdown(10)