d={1:10,2:20}
d1={3:30,4:40}
d2=d.copy()
d2.update(d1)
print(d2)

#or

d3={**d,**d1}
print(d3)