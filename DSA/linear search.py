num=[2,3,4,5,6,7,8,9]
n=len(num)
search=2
def func(num):
    for i in range(0,n):
        if num[i]==search:
            return i
    return -1
ew=func(num)
print(ew)
