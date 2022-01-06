fname=input('Enter a file name: ')
with open(fname) as f:
    a=f.read().split()
max_len = len(max(a, key=len))
result=[word for word in a if len(word) == max_len]
print(result)