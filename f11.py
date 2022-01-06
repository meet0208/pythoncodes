n=int(input('Enter a number: '))
def perfect(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if sum==n:
        return 'number is perfect {}'.format(n)
    else:
        return ' not perfect number'
print(perfect(n))