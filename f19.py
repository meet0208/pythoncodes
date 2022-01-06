def f1(a):
       def f2(b):
              nonlocal a
              a+=1
              return a+b

       return f2
fn=f1(4)
print(fn(4))