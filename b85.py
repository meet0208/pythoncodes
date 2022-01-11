def check(a):
    b=[]
    for i in a:
        b.append(i)
    if len(b)==len(set(b)):
        return True
    else:
        return False
print(check("w3resource"))
print(check(("w3r")))
print(check(("Python")))
print(check(("Java")))