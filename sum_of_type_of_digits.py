num = int(input("Enter number:"))
print("Even digits in the given number are:\n")
even_sum=0
odd_sum=0
while num>0:
    last = num%10
    type = last%2
    if type == 0:
        even_sum = even_sum + last
    if type !=0:
        odd_sum = odd_sum +last
        
    num =num//10
print("Sum of even digits is: ",even_sum)
print("Sum of odd digits is: ",odd_sum)