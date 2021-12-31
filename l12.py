l= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l.pop(0)
l.pop(4)
del l[-1]
print(l)

#or
l= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(l) if i not in (0,4,5)]
print(color)