l=[1,2,3,1,4,5,1]
n=int(input('Enter a number: '))
for (i,ind) in enumerate(l):
    if ind==n:
        print(i , ind)

#or

print(l.index(1))
