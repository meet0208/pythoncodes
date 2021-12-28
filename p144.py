a='meet'
if type(a)==int:
    print('its an integer')
elif type(a)==str:
    print('Its a string')
else:
    pass

#or
print('\n')
print(isinstance(2,int) or isinstance(2,str))
print(isinstance([2],int) or isinstance([2],str))
print(isinstance("2",int) or isinstance("2",str))