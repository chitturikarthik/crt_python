num = int(input("Enter number:"))

print("Odd digits in the given number are:\n")
while num>0:
    last = num%10
    odd = last%2
    if odd != 0:
        print(last)    
    num =num//10
