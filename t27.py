t=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
a=[]
for i in t:
    avg=sum(i)/len(i)
    a.append(avg)
print(a)

# or
nums = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result
print(average_tuple(nums))