n=int(input())
for i in range(n):
    t=int(input())
    a=list(map(int,input().split(" ")))
    pos=0
    for i in range(t):
        if a[i]==1:
            pos=i
            break
        print(pos)
