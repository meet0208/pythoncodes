import cProfile
def sum(a,b):
    print(a+b)
a=int(input('a: '))
b=int(input('b: '))
cProfile.run('sum(a,b)')