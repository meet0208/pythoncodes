t=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
str1=input('Enter a string: ')
def check(a):
    for i in t:
        if a in i:
            return True
        else:
            return False


print(check(str1))