num=[1,1,1,0,0,0,1,0,1,1,1,1]
count=0
max_count=0
n=len(num)

for i in range(0,n):
    if num[i]==1:
        count+=1
        max_count=max(max_count,count)
    else:
        count=0
print(max_count)