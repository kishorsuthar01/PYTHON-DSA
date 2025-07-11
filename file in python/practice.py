# create a new file "practice.txt" using python add the following data in it

with open("practice.txt","w") as f:
    f.write("hello everyone\ni am learning file\nin java\nand programing language")
    
    
# write a function that replace all occurrence of "java" with "python" in above file

with open("practice.txt","r") as f:
    data=f.read()
    print(data)

new_data=data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)



# serach if the word "learning" exist in the file or note

word="learning"
def find():
    with open("practice.txt","r") as f:
     data=f.read()
     if(data.find(word)!=-1):
        print("found")
     else:
        print("not found")

find()
        
    
# write a function  in which line of the file does the word "learning" occurse first.
# print -1 if word not found

def check_line():
    with open("practice.txt","r") as f:
        word="python"
        line=1
        data=True
        while data:
            data=f.readline()
            if(word in data):
                print(line)
                return
            line +=1
    return -1
        
print(check_line())
        
    
# from a file containing number seprated by comma print the count of even number

count=0
with open("number.txt","r") as f:
    data=f.read()
    nums=data.split(",")
    for val in nums:
        if(int(val) % 2==0):
            count+=1
print(count)