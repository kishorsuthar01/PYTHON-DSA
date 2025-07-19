#brute force solution

num=[1,4,5,8,6,7]
n=len(num)
result=13

for i in range(0,n):
    for j in range(i+1,n):
        if num[i]+num[j]==result:
            print(num[i],"+",num[j],"=",result)
            
