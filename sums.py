def isPrime(a):
    if a<2:
        return 0
    for i in range(2,a):
        if a%i==0:
            return 0
    return 1

n = int(input("Enter any number:"))
