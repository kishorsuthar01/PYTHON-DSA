nums=[2,3,4,1,6,8,9,7,5]
n=len(nums)

def func(nums):
    for i in range(n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key

func(nums)
print(nums)