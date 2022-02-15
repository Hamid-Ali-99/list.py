def sum(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i],[j]
nums = [3,1,4,5]
target = 9
res=sum(nums,target)
print(res)

