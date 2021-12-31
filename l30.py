import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
result=dict()
for i in my_list:
    result[i]=result.get(i,0)+1
print(result)

#or

print(collections.Counter(my_list))