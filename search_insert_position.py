a=[1,3,5,6]
target=2
for i in range(len(a)):
    print(a[i])
    if a[i]==target:
        print(a)
    elif a[i]!=target:
        a.append(target)
        a.sort()
print(a)