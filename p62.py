days=int(input('Enter days: '))*3600*24
hours=int(input('Enter hours: '))*3600
minutes=int(input('Enter minutes: '))*60
seconds=int(input('Enter seconds: '))
milliseconds=int(input('Enter milliseconds: '))*0.001
print('Total seconds is:', days+hours+minutes+seconds+milliseconds)