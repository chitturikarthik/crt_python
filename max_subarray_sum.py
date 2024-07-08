nums=[1,2,7,11,15]
target=9
i = 0
a = nums[i]
for i in range(len(nums)):
    if a + nums[i] == 9:
        print(1,i+1)