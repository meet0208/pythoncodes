l=['abc', 'xyz', 'aba', '1221']
count=0
for i in l:
    if len(i)>=2:
        if i[0]==i[-1]:
            count+=1
print(count)