s=input('Enter a string: ')
def palindrom(s):
    s1=s[::-1]
    if s==s1:
        return 'Entered string is palindrom'
    else:
        return 'Not a palindrom'
print(palindrom(s))