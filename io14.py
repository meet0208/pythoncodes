with open('a.txt') as f, open('abc.txt') as d:
    for i,j in zip(f,d):
        print(i+j)