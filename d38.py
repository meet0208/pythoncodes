d={'key1': 1, 'key2': 3, 'key3': 2}
d1={'key1': 1, 'key2': 2}
for (key,value) in set(d.items() & d1.items()):
    print('%s : %s present in both dictionary'%(key,value))