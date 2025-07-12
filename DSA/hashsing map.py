num=[1,2,4,3,6,6,4,8,8,9,67,45,43,3,43]

has_map={}
n=len(num)

for i in range(0,n):
    has_map[num[i]]=has_map.get(num[i],0)+1

print(has_map)