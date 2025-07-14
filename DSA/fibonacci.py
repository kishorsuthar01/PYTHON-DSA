def func(n):
    if n==0 or n==1:
        return n
    return func(n-1)+func(n-2)
num=int(input("enter the number here: "))
if num<0:
    print("enter the positive number")
else:
    print("fibonacci")
for i in range(num):
    print(func(i))