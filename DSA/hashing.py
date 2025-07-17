n=[0,1,2,3,4,5,6,3,4,5,5,2]

m=[2,3,4,5,6,22]

hashing=[0]*11
        

for num in n:
    if num<=0 or num<=10:
        hashing[num]+=1
        
        for num in m:
            if num<=0 or num<=10:
                
                print(f"{num} appears {hashing[num]} time")
            else:
                print(f"{num} appears 0 time (out of range)")

print(hashing)
            
