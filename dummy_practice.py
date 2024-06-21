#Plus One to the number
# n=[1,2,1]
# s=[str(i) for i in n]
# n_str=int("".join(s)) + 1
# print(list(map(int,str(n_str))))

#segments of a string
# name="hello this is karthik"
# data = list(map(str,name.split(" ")))
# print(data)
# count=0
# for i in data:
#     count+=1
# print(count)


# score of a string
# s="chaitanya"
# s_str=list(map(str,s))
# al=list(map(ord,s_str))
# score=0
# for i in range(len(al)-1):
#     score=score+abs(al[i]-al[i+1])
# print(score)

# res=0
# for i in range(1,5):
#     if i%2==0:
#         res+=i
#     else:
#         res-=i
# print(res)


# duplicates
nums=[1,2,3,4,5,6,7,8,9,1]
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]!=nums[j]:
            print("False")
        else:
            print("Tue")