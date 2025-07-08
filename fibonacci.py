def fibo(n):
    if n <=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
num=int(input("enter the number here : "))
if num<=0:
     print("enter the positive number")
else:
    print("fibonacci")
for i in range(num):
       print(fibo(i))
