from operator import itemgetter
l=[('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]

result=max(l,key=itemgetter(1))[1]
minr=min(l,key=itemgetter(1))[1]
print((result,minr))
