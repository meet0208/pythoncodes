l=['1', '2', '3', '4', '5', '6', '7', '8']
l1=[]
for i in range(0,len(l),2):
    l1.append(l[i]+l[i+1])
print(l1)