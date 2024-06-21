def isPrime(a):
    if a<2:
        return 0
    for i in range(2,a):
        if a%i == 0:
            return 0
    return 1

ch=list(map(int,input().split(" ")))
for i in range(len(ch)):
    for j in range(i+1,len(ch)):
        if isPrime(ch[i]):
            ch[i],ch[j]=ch[j],ch[i]
print(ch)