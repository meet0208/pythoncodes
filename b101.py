d={"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14, "Fallon Fabiano": 11, "Nidia Dominique": 15}
l= sorted(d.values(),reverse=True)[0]
for i,j in d.items():
    if j==l:
        print(i)
