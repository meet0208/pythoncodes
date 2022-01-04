from operator import itemgetter
l=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
n=int(input('Position: '))
def sort_list(a,b):
    result=sorted(a,key=itemgetter(b))
    return result
print(sort_list(l,n))