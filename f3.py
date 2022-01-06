t=(8, 2, 3, -1, 7)
def product(l):
    pro=1
    for i in list(l):
        pro*=i
    return pro
print(product(t))