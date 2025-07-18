num=[1,2,3,4,5,6,7,9]
n=len(num)+1

def func(num):
    old=n*(n+1)//2
    new=sum(num)
    return old-new
result=func(num)
print("missing of number is :",result)