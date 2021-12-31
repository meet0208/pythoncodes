import math
a=int(input('1st: '))
b=int(input('2nd: '))
a1=int(input('3rd: '))
b1=int(input('4th: '))
l1,l2=[],[]
print(l1)
l2.append((a1,b1))
def distance(l1,l2):
    output=math.sqrt((l2[0][0]-l1[0][1])**2+(l2[0][0]-l1[0][0])**2)
    return output
print(distance(l1,l2))