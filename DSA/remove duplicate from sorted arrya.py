#brute

num=[1,1,1,2,3,4,4,5,6,7,7,7,8,8,8,9,9]
n=len(num)
dictionary={}

for i in range(0,n):
    dictionary[num[i]]=0
j=0
for k in dictionary:
    num[j]=k
    j+=1
print(dictionary)

#optimal

num=[1,1,1,2,3,4,4,5,6,7,7,7,8,8,8,9,9]
n=len(num)

def func(num):
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if num[j]!=num[i]:
            i+=1
            num[i],num[j]=num[j],num[i]
        j+=1
    return i+1
func(num)
print(num)