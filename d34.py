from collections import Counter
d={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for i in d.values():
    count+=len(i)
print(count)