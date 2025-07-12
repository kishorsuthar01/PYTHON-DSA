num=[1,2,4,3,6,6,4,8,8,9,67,45,43,3,43]

freq_map={}

for i in range(0,len(num)):
    if num[i] in freq_map:
        freq_map[num[i]]+=1
    else:
        freq_map[num[i]]=1

print(freq_map)
