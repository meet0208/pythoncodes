l=[1,2,3,45,'meet',(1,2),2,3]
count=0
for i in l:
    if type(i)!=tuple:
        count+=1
    else:
        break
print(count)