str=input("Enter the string:")
chair=0
max_chairs=0
for i in range(len(str)):
    if str[i].lower() == 'e':
        chair+=1
        max_chairs=max(chair,max_chairs)
    elif str[i].lower() == 'l':
        chair-=1
        max_chairs=max(chair,max_chairs)
print("Maximum no. of required chairs: ",max_chairs)