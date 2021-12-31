l=[1, 3, 5, 7, 9, 10]
l1=[2, 4, 6, 8]
l.remove(l[-1])
l.extend(l1)
print(l)

#or

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)