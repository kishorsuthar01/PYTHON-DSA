num=[23,4,23,67,67,-65,445]
n=len(num)
largest=num[0]
for i in range(0,n):
    largest=min(largest,num[i])

print(largest)