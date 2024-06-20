# li=list(map(int,input("Enter colors:").split(",")))
# for i in range(0,len(li)):
#     for j in range(i+1,len(li)):
#         # if li[j]>li[i]:
#         #     li[i],li[j]= li[j],li[i]
#         if li[j]<li[i]:
#             li[j],li[i]=li[i],li[j]
# print(li)
a=[2,0,1,0,2,1]
low=0
high=len(a)-1
mid=0

while mid<high:
    if a[mid]==2:
        a[mid],a[high]=a[high],a[mid]
        high-=1
    elif a[mid]==0:
        a[mid],a[low]=a[low],a[mid]
        low+=1
        mid+=1
    else:
        mid+=1   
print(a)