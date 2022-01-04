l=[0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
n=int(input('Enter a number: '))
c=int(input('Enter count: '))
if l.count(n)==c:
    print(True)
else:
    print(False)