from timeit import default_timer
def timer(n):
    start = default_timer()
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(4)
timer(15)
