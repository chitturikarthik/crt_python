def reverse(num):
    rev=0
    while num>0:
        rev=(rev*10)+(num%10)
        num=num//10
    print(rev)
    return rev
    
n=int(input("Enter a number:"))
perfect=reverse(n)
if n==perfect:
    print("The number is palindrome and a perfect number")
else:
    print("The number is not palindrome and not a perfect number")