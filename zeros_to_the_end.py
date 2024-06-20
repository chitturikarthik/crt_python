n=list(map(int,input("").split(" ")))
i=0
j=0
temp=0
while j<len(n):
    if n[j]!=0:
        temp=n[i]
        n[i]=n[j]
        n[j]=temp
        # n[i],n[j]=n[j],n[i]
        i+=1
        j+=1
    else:
        j+=1
print(n)