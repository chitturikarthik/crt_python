a=[4,6,8,5,3,5,2,7,2,2]
d={}
for elements in d:
    if elements in a:
        d[elements]+=1
    else:
        d[elements]=1
for key,value in d.items():
    if value==3:
        print(key)