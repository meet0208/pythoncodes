def symmetrical(a):
    b=str(a)
    if b==b[::-1]:
        return True
    else:
        return False
print(symmetrical(121))
print(symmetrical(0))
print(symmetrical(122))
print(symmetrical(990099))