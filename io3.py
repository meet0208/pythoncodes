fname=input('Enter a file name: ')
with open(fname,'w') as f:
    f.write('Meet Boghani')
txt = open(fname)
print(txt.read())