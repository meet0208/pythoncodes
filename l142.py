l=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
n=int(input('Enter column number: '))
sum=0
for i in l:
    sum+=i[n]
print(sum)
