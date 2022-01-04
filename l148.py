l=['red', 'green', 'blue', 'white', 'black', 'orange']
l1=['white', 'orange']
for i in l:
    if i in l1:
        l.remove(i)
print(l)