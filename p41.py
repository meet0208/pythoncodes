fname=open('p4.py')
try:
    fname.close()
    print('file found')
except FileNotFoundError:
    print('not found')
