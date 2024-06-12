num = int(input("Enter number:"))
print("Even digits in the given number are:\n")
even_pro=1
odd_pro=1
while num>0:
    last = num%10
    type = last%2
    if type == 0:
        even_pro = even_pro * last
    if type !=0:
        odd_pro = odd_pro * last
        
    num =num//10
print("Product of even digits is: ",even_pro)
print("Product of odd digits is: ",odd_pro)