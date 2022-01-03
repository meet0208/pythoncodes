l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
str=input('Direction left or right: ')
n=int(input('Enter a specified number: '))
if str=='left':
    result=l[n:]+l[:n]
    print(result)
elif str=='right':
    result1=l[-n:]+l[:-n]
    print(result1)
