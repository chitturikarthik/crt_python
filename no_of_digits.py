#Program to find out number of digits in a number without using len() function
num = int(input("Enter any number:"))
count = 0
while(num>0):
    count+=1
    num=num//10 #float divison
    print(count)

print(f"No. of digits in the given number is {count}")