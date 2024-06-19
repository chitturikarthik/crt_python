n=list(map(int,input("Enter array elements:").split(",")))
print(n)
size=0
count=0
for i in n:
    size+=1

for num in n:
    if n.count(num)>= (size//2):
        print(num)