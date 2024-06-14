n=int((input("Enter a number:")))
sum=0
while n>0:
    d=n%10
    sum=sum*10+d
    print(sum)
    n=n//10
print("Reversed Number:",sum)