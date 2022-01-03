l=[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
left=13
right=17
for i in l:
        if min(i)>=left and max(i)<=right:
            print(i)

