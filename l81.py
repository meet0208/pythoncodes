import random
l=[1,1,2,3,4,4,5,1]
n=int(input('Enter number of elements need to select randomly: '))
result=random.sample(l,n)
print(result)

#or

l1=[]
for i in range(n):
    l1.append(random.choice(l))
print(l1)