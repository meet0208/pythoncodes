num=int(input('enter a number: '))
list1=[1,2,3,4,5]
def tocheck(a,b):
    if b in a:
        return True
    else:
        return False
print(tocheck(list1,num))