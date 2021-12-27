import math
from functools import reduce
l1=[1,25,54,2,1]
print(math.prod(l1))
pro=reduce((lambda x,y:x*y), l1)
print(pro)
