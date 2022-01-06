n=abs(int(input('Enter a number: ')))
def factorial(n):
    pro=1
    for i in range(1,n+1):
        pro*=i
    return pro
print( factorial(n))