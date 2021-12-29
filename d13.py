keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
d={}
for i in range(len(keys)):
    d[keys[i]]=values[i]
print(d)

#or
d1=dict(zip(keys,values))
print(d1)