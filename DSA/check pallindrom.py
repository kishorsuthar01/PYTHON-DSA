
#using recursion

name="nitin"
def func(name,left,right):
    if left>=right:
        return True
    if name[left]!=name[right]:
        return False
    return func(name,left+1,right-1)

result=func(name,0,len(name)-1)
print(result)


#using for-loop

name="kishor"
def func(name,left,right):
    for i in range(len(name)):
        if left>=right:
            return True
        if name[left]!=name[right]:
            return False
        return func(name,left+1,right-1)
result=func(name,0,len(name)-1)
print(result)


#using while-loop

name="nitin2"
def func(name,left,right):
    while left>=right:
        return True
    if name[left]!=name[right]:
        return False
    return func(name,left+1,right-1)

result=func(name,0,len(name)-1)
print(result)