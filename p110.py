a=[1,15,30,25,60,125]
print([i for i in a if i%15==0])
print(list(filter(lambda x:(x%15==0),a)))