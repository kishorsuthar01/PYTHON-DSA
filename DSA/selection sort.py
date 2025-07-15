#selection sort

nums=[1,3,5,7,9,8,6,4,2,0]
n=len(nums)
def func(nums):
    for i in range(0,n):
        min_idx=i
        for j in range(i+1,n):
            if nums[j]<nums[min_idx]:
                min_idx=j
            nums[i],nums[min_idx]=nums[min_idx],nums[i]
func(nums)
print(nums)



