def isValid(num):
    count=0
    while num>0:
        count+=1
        num=num//10
    return count
    
def isTrendy(num):
    md=(num//10)%10
    if md%3 == 0:
        print(md)
        return 1
    else:
        return 0
    
n=int(input("Enter a number:"))
if isValid(n) != 3: 
    print("Trendy number must be of length 3")
elif isTrendy(n):
    print(f"{n} is a trendy number")
else:
    print(f"{n} is not trendy")