#brute force solution

arr=[1,2,3,4,5,6,7,8]
n=len(arr)
k=4
rotation=k%n

for i in range(0,rotation):
    e=arr.pop()
    arr.insert(0,e)
print(arr)

#better solution

arr=[1,2,3,4,5,6,7,8]
n=len(arr)
k=2

arr[:]=arr[n-k:]+arr[:n-k]
print(arr)


#optimal solution

arr=[1,2,3,4,5,6,7,8]
n=len(arr)
k=5
def func(arr,left,right):
    if left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
func(arr,n-k,n-1)
func(arr,0,n-k-1)
func(arr,0,n-1)
print(arr)