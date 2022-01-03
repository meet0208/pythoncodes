from itertools import groupby
def encode_list(s_list):
    def cot(a):
        if len(a)>1:
            return [len(a), a[0]]
        else: return a[0]
    return [cot((list(group))) for key, group in groupby(s_list)]
n_list = [1, 1, 2, 3, 4, 4, 5, 1]
print(encode_list(n_list))