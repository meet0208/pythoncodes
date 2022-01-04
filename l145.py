import random
srange=int(input('Enter starting range: '))
erange=int(input('Enter ending range: '))
def ch(s,e):
    result=random.choice([i for i in range(s,e) if i not in [2, 9, 10]])
    return result
print(ch(srange,erange))
