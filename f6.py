n=int(input('Enter a number: '))
def check(n):
    if n in range(1,10):
        return True
    else:
        return False
print(check(n))