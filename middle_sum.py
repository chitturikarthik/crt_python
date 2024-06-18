def minMax(arr):
    for num in arr:
        i=list(arr[num])
        max_value=max(i)
        min_value=min(i)
        print(max_value,min_value)
        
n=list(map(int,input("Enter list elements:").split(" ")))
values=minMax(n)
print(values)
            