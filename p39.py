amount=float(input('amount: '))
interest=float(input('interest: '))
years=float(input('Years: '))
value=amount*(1+(interest/100))**years
print('future value is {:.2f}'.format(value))