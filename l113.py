d=[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

result=[dict(e) for e in {tuple(i.items()) for i in d }]
print(result)
