try:
    x = 29
except NameError:
    print('Variable not defined: ')
else:
    print('Variable defined')

try:
    y
except NameError:
    print('Variable not defined: ')
else:
    print('Variable defined')
