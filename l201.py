str1='https://www.w3resource.com/python-exercises/list/'
l=['.com', '.edu', '.tv']
result = [el for el in l if(el in str1)]
print(bool(result))
l1=[]
for i in l:
    if i in str1:
        print(True)
    else:
        pass