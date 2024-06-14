print("Available candies are 20")
while True:
    N=20#max capacity of candies in the jar
    min_candies=4#min candies should be present in the jar
    sold=0
    req=int(input("Enter number of candies you want:"))
    if req>N:
        print("Invalid Input,try again!")
    else:
        sold=N-req
        print("Candies Sold:",req)
        print("Candies remaining:",sold)

    print("New Candies:",N)
    cont = input("Do you still want some candies(y/n):")
    if cont.lower() == 'n':
        break
        
