#using recorsion 

arr=[1,2,4,5,6,7,8,9,23,4,55]

def func(nums,left,right):
    if left>right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    func(arr,left+1,right-1)
func(arr,0,len(arr)-1)
print("reverse ",arr)


#using for-loop

arr=[1,2,4,5,6,7,8,9,23,4,55]

def func(arr,L,R):
    for i in range(len(arr)):
        if L>R:
            return
        arr[L],arr[R]=arr[R],arr[L]
        func(arr,L+1,R-1)

func(arr,0,len(arr)-1)
print("reverse ",arr)


#using while-loop

arr=[1,2,4,5,6,7,8,9,23,4,55]

def func(arr,L,R):
    while L>R:
        return
    arr[L],arr[R]=arr[R],arr[L]
    func(arr,L+1,R-1)

func(arr,0,len(arr)-1)
print("reverse ",arr)