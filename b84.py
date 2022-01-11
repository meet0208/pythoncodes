def check(a):
    ctr=0
    sum=0
    for i in a:
        if i<0:
            ctr+=1
        else:
            sum+=i
    return [ctr,sum]
print(check([1, 2, 3, 4, 5]))
print(check([-1, -2, -3, -4, -5]))
print(check([1, 2, 3, -4, -5]))
print(check([1, 2, -3, -4, -5]))