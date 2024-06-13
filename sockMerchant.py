#Alex works at a clothin stroe. Ther is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

def sockMerchant(n,arr):
    pairs=0
    set_arr=set(arr)
    for i in set_arr:
        count=arr.count(i)
        pairs+=count//2
    return pairs

n=int(input("Enter number of socks:"))
arr=list(map(int,input("Enter colors of socks:").split(" ")))
print(sockMerchant(n,arr))