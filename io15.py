from random import choice
with open('io1.py') as f:
    l=f.read().split()
    print(choice(l))