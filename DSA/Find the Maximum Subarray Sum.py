num=[1,4,-3,-6,4,8,9,-2]
total=0
maxi=float("-inf")
n=len(num)
for i in range(0,n):
    total=0
    for j in range(i,n):
        total=total+num[j]
        maxi=max(maxi,total)
        if total<0:
            total=0
print(maxi)