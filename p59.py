height=float(input('height in feet: '))
height1=float(input('height in inches: '))
h1=height*30.48
h2=height1*2.54
h=int(h1+h2)
print('height in centimeter: {} cm'.format(h))
