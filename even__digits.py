num = int(input("Enter number:"))

print("Even digits in the given number are:\n")

while num>0:
    last = num%10
    even = last%2
    if even == 0:
        print(last)
    num =num//10