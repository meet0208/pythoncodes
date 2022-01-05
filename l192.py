l=[(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]

result=[tuple(j for j in i if isinstance(j,int))for i in l]

print(result)