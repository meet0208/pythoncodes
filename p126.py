from inspect import getmodule
from math import sqrt

def add(x, y):
    return x + y
print(getmodule(add))
print(getmodule(sqrt))