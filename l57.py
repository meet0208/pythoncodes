color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]
s=input('Enter a string: ')
def check(a,s):

    if all(i==s  for i in a):
        return True
    else:
            return False

print(check(color1,s))
print(check(color2,s))