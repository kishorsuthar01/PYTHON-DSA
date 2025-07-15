
nums=[3,4,2,1,5,6,7,9,8,0]
n=len(nums)

def func(nums):
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
func(nums)
print(nums)