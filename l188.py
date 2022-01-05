l=[('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
n=int(input('Enter a position: '))
result = sorted((l), key=lambda x: x[n])
print(result)