a=[1,2,34,3,4,5,7,23,12]    
for i in range(len(a)):
    if a[i]%2 != 0 and a[i+1]%2 !=0 and a[i+2]%2 !=0:
        print(a[i],a[i+1],a[i+2])