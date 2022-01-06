numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
ctr = 0
ctr1 = 0
for i in numbers:
    if i%2==0:
        ctr+=1
    else:
        ctr1+=1

print(ctr)
print(ctr1)