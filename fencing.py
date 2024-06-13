#Take input from user about lenght and breadth of a rectangular field and calculate the fencing required to fence the field
while 1:
    length = int(input("Enter the length of the field:"))
    breadth= int(input("Enter the breadth of the field:"))
    fencing = 2*(length+breadth)
    print("Fencing required is:",fencing)
    cont= input("Do you want to continue(y/n):")
    if cont.lower() != 'y':
        exit()