l=['0', '1', '2', '3', '4']
l1=['red', 'green', 'black', 'blue', 'white']
l2=['100', '200', '300', '400', '500']
l3=[]
for (i,j,k) in zip(l,l1,l2):
    l3.append(i+j+k)
print(l3)