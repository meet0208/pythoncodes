student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}
d={}
for key,value in student_data.items():
    if value not in d.values():
        d[key]=value
print(d)