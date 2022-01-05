l=[('red', 'green'), ('black', 'white'), ('orange', 'pink')]
result = [("%s "*len(el)%el).strip() for el in l]
print(result)
