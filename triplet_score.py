a=list(map(int,input().split()))
b=list(map(int,input().split()))
ac=0
bc=0
for i in range(len(a)):
    if a[i]>b[i]:
        ac+=1
    elif a[i]<b[i]:
        bc+=1
 