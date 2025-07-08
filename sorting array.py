list=[2,4,1,23,12,54,64,122,43,87,0]
n=len(list)
for i in range(n):
     for j in range(i+1,n):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
    