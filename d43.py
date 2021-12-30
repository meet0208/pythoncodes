l=['S001', 'S002', 'S003', 'S004']
l1=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l2= [85, 98, 89, 92]
print([{i:{j:k}} for i,j,k in zip(l,l1,l2)])
