n=int(input("Enter a big number:"))
k=int(input("Enter a single digit:"))
count=0
while n>0:
    ld=n%10
    if ld%k == 0:
        count +=1
    n=n//10
print("Digits in the number divisible by k are :",count)