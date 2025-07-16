arr=[23,4,23,134,75,88,98]
largest=arr[0]
n=len(arr)
for i in range(0,n):
    largest=max(largest,arr[i])
print(largest)