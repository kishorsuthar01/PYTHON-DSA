num=[1,4,3,5,6,7,10,-1,11]
n=len(num)
tem=num[n-1]
for i in range(n-2,-1,-1):
    num[i+1]=num[i]
num[0]=tem
print(num)
        