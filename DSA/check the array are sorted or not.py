num=[1,2,3,7,4,5]
n=len(num)
def func(num):
 for i in range(0,n-1):
    if num[i]>num[i+1]:
        return False
 return True
re=func(num)
print(re)