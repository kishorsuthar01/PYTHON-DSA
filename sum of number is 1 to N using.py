num=int(input("Enter the number :"))
sum=0

for i in range(1,num+1):
    print(i)
    sum+=i
    i+=1
    
print("the total of number is ",sum)