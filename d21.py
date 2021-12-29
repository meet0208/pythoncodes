from itertools import product
Sample = {'1':['a','b'], '2':['c','d']}
for x ,y in product(*Sample.values()):
    print(''.join(x+y))

