l = [22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]
s=sum(map(round,l))
print(s*len(l))

#or

sum=0
for i in l:
    sum+=round(i)
print(sum*len(l))