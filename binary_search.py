def binary(arr,t):
    l=0
    h=len(arr)-1
    # mid=0
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==t:
            print(mid)
        elif arr[mid]>t:
            h=mid-1
        elif arr[mid]<t:
            l=mid+1
        print(l)

ch=[2,6,3,10,8,12]
ch.sort()
print(ch)
t=7
binary(ch,t)