def isTriangle(s1,s2,s3):
    return s1+s2>s3 and s3+s2>s1 and s1+s3>s2
    
a=int(input("Enter Side 1:"))
b=int(input("Enter Side 2:"))
c=int(input("Enter Side 3:"))
if isTriangle(a,b,c):
    print("The triangle can be formed with the given sides!")