# ch=[4,2,6,3,8]
# res=[]
# diff=0
# for i in range(1,len(ch)):
#     diff=abs(ch[i]-ch[i-1])
#     res.append(diff)
# print(res)
# print(min(res))

# Approach with max function
ch=[4,2,6,8,12]
min1=1
for i in range(1,len(ch)):
    min1=min(min1,abs(ch[i]-ch[i-1]))
print(min1)