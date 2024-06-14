# n = int(input("Enter a number:"))
# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")5


# n = int(input())
# for i in range(0,n):
#     print(i)
#     print(i*i)

n=int(input("_____"))
num=0
for i in range(1,n+1):
    rem=i
    num=num*10+rem
print(num)