def isPrime(a):
    if a<2:
        return 0
    for i in range(2,a):
        if a%i==0:
            return 0
    return 1

num = int(input("Enter a number:"))
print("Prime digits in the given number are:")
sum =0
prod = 1
while num:
    ld = num%10
    if isPrime(ld):
        print(f"{ld} is a prime digit")
        sum = sum + ld
        prod = prod * ld
    else:
        print(f"{ld} is not prime")
    num=num//10
print(f"Sum of primes is : {sum}")
print(f"Product of primes is : {prod}")