#Take temperature readings from user cotinuously and display +ve, -ve and zero temperatures
while True:
    temp = int(input("Enter Temperatrue value:"))
    if temp>0:
        print("Temperature is positive")
    elif temp<0:
        print("Temperature is negative")
    else:
        print("Temperature is zero")
    cont = input("Do you want to continue(y/n):")
    if cont.lower() != 'y':
        break