n=int(input('Enter a number: '))
def prime(n):
    ctr=0
    for i in range(1,n+1):
        if n%i==0:
            ctr+=1
        else:
            pass
    if ctr==2:
        return 'number is prime',n
    else:
        return 'Not prime number'
print(prime(n))