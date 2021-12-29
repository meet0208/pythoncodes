d={1:10,2:20,3:30}
d1={}
def check(a):
    if a.values():
        print('Not empty')
    else:
        print('Empty')

check(d)
check(d1)