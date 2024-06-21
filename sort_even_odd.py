
# for i in range(0,len(ch)):
#     for j in range(i+1,len(ch)):
#         if ch[i]%2 != 0:
#             ch[j],ch[i]=ch[i],ch[j]
# print(ch)
            
#Approach2
ch=list(map(int,input().split()))
even=0
odd=len(ch)-1
while even<odd:
    while ch[even]%2 == 0 and even<odd:
        even+=1
    while ch[odd]%2 != 0:
        odd-=1
    if even<odd:
        ch[even],ch[odd]=ch[odd],ch[even]
print(ch)