import os
print('Effective id:',os.getegid())
print('Effective User id:',os.geteuid())
print('Real id:',os.getgid())
print('list of supplemental group ids:', os.getgroups())