a=[0,0,1,1,2,2,3,3,4,4]
j=1
for i in range(1,len(a)):
    if a[i]!=a[i-1]:
        a[j]=a[i]
        j+=1
        print(j)
print(j)