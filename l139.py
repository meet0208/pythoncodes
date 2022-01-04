l=['4', '12','45', '7', '0', '100', '200', '-12', '-500']
result=[int(i) for i in l]
result.sort()
print(result)
l=[str(i) for i in result]
print(l)