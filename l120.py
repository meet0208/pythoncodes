l=['red', 'black', 'white', 'green', 'orange']
def alt(a):
    result=[i for i in a[::2]]
    return result

print(alt(l))