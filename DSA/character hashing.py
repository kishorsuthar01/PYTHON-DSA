A="aabbrccdrdrabc"
B=["a","b","c","d","r"]

character=[0]*26
for i in A:
    ascii=ord(i)
    index=ascii-97
    character[index]+=1
    
for i in B:
    ascii=ord(i)
    index=ascii-97
    print(character[index])
    

print(character)