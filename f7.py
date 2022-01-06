s='The quick Brow Fox'
def u_l_check(s):
    ctr,ctr1=0,0
    for i in s:
        if i.isupper():
            ctr+=1
        elif i.islower():
            ctr1+=1
    return (ctr,ctr1)
print(u_l_check(s))