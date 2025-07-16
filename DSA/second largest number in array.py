arr=[23,4,23,134,75,88,98]
largest=arr[0]
second_largest=arr[0]
n=len(arr)
for i in range(0,n):
    largest=max(largest,arr[i])
    
for i in range(0,n):
    if arr[i]>second_largest and arr[i]!=largest:
        second_largest=arr[i]

print(largest)
print(second_largest)
    
