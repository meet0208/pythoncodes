l=['Python', 'list', 'exercises', 'practice', 'solution']
n=int(input('Enter a specific length: '))
l1=[]
for i in l:
    if len(i)==n:
        l1.append(i)
print(l1)