l=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
l1=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
if len(l)==len(l1):

        result=[i+j for (i,j) in zip(l,l1)]
print(result)