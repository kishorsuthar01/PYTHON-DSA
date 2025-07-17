arr=[1,2,3,4,5,7,9,5,8,77,89]
n=len(arr)
def func(arr):
 for i in range(0,n-1):
     if arr[i]>arr[i+1]:
         return False
 return True
func(arr)
arr.sort()
print(arr)