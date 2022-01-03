l=['Python', 3, 2, 4, 5, 'version']
l1=[]
mi=min(i for i in l if isinstance(i,int))
ma=max(i for i in l if isinstance(i,int))
print((ma,mi))