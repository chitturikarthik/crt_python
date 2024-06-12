#Program to find out number of digits in a number without using len() function
num = int(input("Enter any number:"))
sum = 0
while(num>0):
    last = num%10
    sum = sum + last
    num = num//10
    print(f"SUM:{sum} , LAST DIGIT:{last}")

print(f"Sum of digits in the given number is {sum}")