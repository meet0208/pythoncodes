l=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
from itertools import groupby
def compress(l_nums):
    return [key for key, group in groupby(l_nums)]
print(compress(l))