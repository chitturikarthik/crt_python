def getMinMax(n):
    mind=9
    maxd=0
    while n:
        ld=n%10
        if mind>ld:
            mind=ld
        if maxd<ld:
            maxd=ld
        n=n//10        
    return (mind,maxd)
            

def DigitSum(num):
    mind,maxd=getMinMax(num)
    dsum=0
    while num:
        ld=num%10
        if ld!=mind and ld!=maxd:
            dsum = dsum+ld
        num=num//10
    return dsum
        
a=[1223,457,234,345]
result=0
for i in a:
     result=result+DigitSum(i)    
print(result)