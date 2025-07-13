list=[23,5,2,3,5,87,12,43,0]
max=list[0]
min=list[0]

for i in list:
     if i>max:
        max=i
     if i<min:
        min=i
print(max)
print(min)