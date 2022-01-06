from shutil import copyfile
fname='a.txt'
fname1='abc.txt'
copyfile(fname,fname1)
a=open(fname1)
print(a.read())