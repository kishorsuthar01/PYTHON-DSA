#brute force solution

num=[3,9,5,6,7,5,3,2]
n=len(num)
k=3

rotation=k%n
for i in range(0,rotation):
    e=num.pop()
    num.insert(0,e)
print(num)


#better solution

num=[3,9,5,6,7,5,3,2]
n=len(num)
k=3
k=k%n
num[:]=num[n-k:]+num[:n-k]
print(num)


#optiomal solution



num=[3,9,5,6,7,5,3,2]
n=len(num)
k=5

def func(num,left,right):
    while left<right:
        num[left],num[right]=num[right],num[left]
        left+=1
        right-=1

func(num,n-k,n-1)
func(num,0,n-k-1)
func(num,0,len(num)-1)
print(num)