l=[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
l1=[2, 4, 6, 8, 10, 12, 14]
def unique(a):
   if len(a)==len(set(a)):
       return True
   else:
       return False

print('List is unique:', unique(l))
print('List is unique:', unique(l1))