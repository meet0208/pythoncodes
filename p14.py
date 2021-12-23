from datetime import date
t1,t2=[],[]
for i in range(0,3):
    v=int(input('Values: '))
    t1.append(v)
t1=date(*tuple(t1))
for i in range(0,3):
    v1=int(input('Values: '))
    t2.append(v1)
t2=date(*tuple(t2))
print((t2-t1).days)