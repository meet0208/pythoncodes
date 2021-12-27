def Empty_Var(lst):
   return [type(i)() for i in lst]
lst = ["python",{"x":12},[10,12,"sfsd"], (4,5), 200]
print("Original objects:")
print(lst)
print("\nEmpty the said variables without destroying it:")
print(Empty_Var(lst))

n = 29
d = {"x":"meet"}
l = [1,2,3,4]
t= (5,6,7,8)
print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())