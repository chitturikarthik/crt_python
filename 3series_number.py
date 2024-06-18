def isPattern(arr,t):
    for i in range(len(arr)-2):
        if arr[i]==t and arr[i+1]==t and arr[i+2]==t:
            return 1
        
li=list(map(int,input("Enter numbers:").split(" ")))
print(li)
num=int(input("Enter target number:"))
if isPattern(li,num):
    print("Pattern found!")
else:
    print("Pattern not found!")