nums=list(map(int,input("Enter array elements:").split(" ")))
nums.sort()
res1=nums[-1]*nums[-2]*nums[-3]
res2=nums[0]*nums[1]*nums[-1]
prod=max(res1,res2)
print(prod)