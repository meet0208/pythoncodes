n=int(input('Enter 1st value: '))
n1=int(input('Enter 2nd value: '))
n2=int(input('Enter 3rd value: '))
sum=0
if n==n1==n2:
    sum+=(n+n1+n2)*3
    print(sum)
else:
    sum+=(n+n1+n2)
    print(sum)