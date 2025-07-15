A=[1,5,8,2]
B=[4,3,6,7,9]

def merge(left,right):
    result=[]
    i,j=0,0
    A,B=len(left),len(right)
    
    while i<A and j<B:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<A:
        result.append(left[i])
        i+=1
    else :
        result.append(right[j])
        j+=1
    return result

A.sort()
B.sort()

merged=merge(A,B)
print(merged)

# ..........................................................................

arr=[2,3,4,1,6,9,7,8,5]

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)
    return merge_sort(left_half,right_half)
arr.sort()
print(arr)