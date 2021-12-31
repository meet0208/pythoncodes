l=[1,2,3,4,5]
l1=[1,10,1,5,12]
def check(l,l1):
    for i in l:
        for y in l1:
            if i==y:
                return True
                break
            else:
                return False
print(check(l,l1))