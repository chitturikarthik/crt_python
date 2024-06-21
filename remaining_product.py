
#approach1
# r=[]
# for i in range(len(a)):
#     pro=1
#     for j in range(len(a)):
#         if a[i]!=a[j]:
#             pro=pro*a[j]
#     r.append(pro)
# print(r)
#approach2
a=list(map(int,input().split()))
pro=1
for i in a:
    pro=pro*i
for i in range(len(a)):
    print(a[i])
    a[i]=pro//a[i]
print(a)
    