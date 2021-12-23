str1=input('string: ')
def parsecheck(a):
    try:
       return int(str1)
    except ValueError:

        return float(str1)

print(parsecheck(str1))