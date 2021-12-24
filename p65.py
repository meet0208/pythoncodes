seconds=int(input('Enter seconds: '))
days=seconds/(3600*24)
hours=seconds/3600
minutes=seconds/60
seconds=seconds
print('Days: {0}, Hours: {1}, Minutes: {2}, Seconds: {3}'.format(days,hours,minutes,seconds))