from random import shuffle
l=['Python', 'list', 'exercises', 'practice', 'solution']
l1=[]
for i in l:
    i =list(i)
    shuffle(i)
    b=''.join(i)
    l1.append(b)
print(l1)