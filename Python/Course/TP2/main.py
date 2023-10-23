import sys
import constants

from random import randint
from pprint import pprint

name = __name__

def random_number():
    return randint(1, 100)

def get_modules():
    return sys.path

def get_pi_constants():
    return constants.PI

if name == '__main__':
    # print(random_number())
    # pprint(get_modules())
    print(get_pi_constants())