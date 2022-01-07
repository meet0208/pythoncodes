s=input('Enter a string: ')
ctr=0
ctr1=0
for i in s:
    if i.isdigit():
        ctr+=1
    elif i.isalpha():
        ctr1+=1
print(ctr)
print(ctr1)