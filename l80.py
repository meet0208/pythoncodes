l=[1, 1, 2, 3, 4, 4, 5, 1]
print('Enter value and index for new element: ')
a,b=map(int,input().split())
l.insert(b,a)
print(l)