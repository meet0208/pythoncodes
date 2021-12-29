class dictionary:
    def __init__(meet):
        meet.x=1
        meet.y=2
        meet.z=3

    def obj(meet):
        a=meet.x
        b=meet.y
        c=meet.z
        print(a,b,c)
t=dictionary()
t.obj()
print(t.__dict__)