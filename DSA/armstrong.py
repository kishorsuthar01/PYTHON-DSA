n=121
num=n
total=0
digite=len(str(n))

while num>0:
    last_d=num%10
    total=total+(digite**last_d)
    num=num//10
if(total==n):
    print("True")
else:
    print("f")