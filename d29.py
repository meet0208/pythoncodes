student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d={}
for i,j in student_list.items():
    i=i.replace(' ','')
    d[i]=j
print(d)