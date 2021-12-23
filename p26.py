s=input('any string: ')
n=int(input('Range: '))
l1=[]
for i in range(0,n):
    a=int(input())
    l1.append(a)
for i in l1:
    print('\t')
    for j in range(0,i):
        print(s,end='')