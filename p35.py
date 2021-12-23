n=int(input('Enter 1st value: '))
n1=int(input('Enter 2nd value: '))
def check(n,n1):
    sum = n + n1
    diff = n - n1
    if n==n1 or sum==5 or diff == 5:
        return True
    else:
        return False
print(check(n,n1))