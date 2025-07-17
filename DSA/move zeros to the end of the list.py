
#brute force solution
num=[1,0,2,4,0,0,5,8,0,2,3,5]
n=len(num)
temp=[]

for i in range(0,n):
    if num[i]!=0:
        temp.append(num[i])
n2=len(temp)
for i in range(0,n2):
    num[i]=temp[i]
for i in range(n2,n):
    num[i]=0
print(num)


#optimal solution

num=[1,0,2,4,0,0,5,8,0,2,3,5]
n=len(num)
i=0
j=i+1

while i<n:
    if num[i]==0:
        break
    i+=1
    if i==n:
        break
while j<n:
    if num[j]!=0:
        num[i],num[j]=num[j],num[i]
        i+=1
    j+=1
print(num)