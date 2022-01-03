l=[{},{},{}]
my_list1 = [{1,2},{},{}]
print(all(i!=None for i in l))
print(all(not i for i in l))
print(all(not i for i in my_list1))
