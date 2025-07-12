#factors using function

# def factor(x):
#     for i in range(1,x+1):
#         if x%i==0:
#             print(i)
# num=10
# factor(num)


num=int(input("enter the number here :"))

#using for loop
result=[]
for val in range(1,num+1):
    if num %val==0:
        result.append(val)
print(result)

#using while loop

# i=1

# while i<=num:
#     if num%i==0:
#         print(i)
#     i+=1
    