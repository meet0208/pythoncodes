a=['meet']
if type(a)==list:
    print('Its a list')
elif type(a)==tuple:
    print('Its a tuple')
elif type(a)==set:
    print('Its a set')
else:
    pass

#or

print('\n')
print(isinstance((2,'meet'),tuple) or isinstance((2),list) or isinstance((2),set))
print(isinstance([2],tuple) or isinstance([2],list) or isinstance([2],set))
print(isinstance({2},tuple) or isinstance({2},list) or isinstance({2},set))