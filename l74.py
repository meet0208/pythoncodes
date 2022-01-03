from itertools import groupby
l=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
def pack_consecutive_duplicates(l_nums):
    return [list(group) for key, group in groupby(l_nums)]
print(pack_consecutive_duplicates(l))