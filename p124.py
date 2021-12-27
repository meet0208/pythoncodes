x='meet'
y=10
z=11
if x==y==z:
    print('same value')
else:
    print('no same value')

#or

def multiple_variables_equality(*args):
   for x in args:
       if x != args[0]:
           return "All variables have not same value."
   return "All variables have same value."
print(multiple_variables_equality(2,3,2,2,2,2))
print(multiple_variables_equality(10,10,10,10))
print(multiple_variables_equality(-3,-3,-3,-3))