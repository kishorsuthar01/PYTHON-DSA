#brute force solution

num=[1,2,3,4,0,0,8,0,5,0,0,4]
n=len(num)
temp=[]
for i in range(0,n):
    if num[i]!=0:
        temp.append(num[i])
n1=len(temp)
for i in range(0,n1):
    num[i]=temp[i]
for i in range(n1,n):
    num[i]=0
print(num)

#optimal solution

num=[1,2,3,4,0,0,8,0,5,0,0,4]
n=len(num)
i=0
j=i+1

for i in range(0,n):
    if num[i]==0:
        break
    if i==n:
        break
for j in range(i+1,n):
    if num[j]!=0:
        num[i],num[j]=num[j],num[i]
        i+=1
    j+=1
print(num)