#Program to find out product of digits in a number without using len() function
num = int(input("Enter any number:"))
prod = 1
while(num>0):
    last = num%10
    prod = (prod * last)
    num = num//10
    print(f"Product:{prod} , LAST DIGIT:{last}")

print(f"Product of digits in the given number is {prod}")