import os
fname=input("Enter file name: ")
a=os.path.abspath(fname)
b=tuple(a.split('.'))
print(os.path.splitext(a))
print(b)