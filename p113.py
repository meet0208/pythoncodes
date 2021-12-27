try:
    num = float(input('Enter a number:'))
    print(num)
except ValueError:
    print('Not a number')