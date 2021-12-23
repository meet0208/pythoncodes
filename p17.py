n=int(input('Enter a number: '))
def check(n):
    if (abs(1000-n)<=100) or (abs(2000-n)<=100):
        return True

    else:
        return False

print(check(n))