f = open("demo.txt","r")

data=f.read()
print(data)


line1=f.readlines()
print(line1)

line2=f.readlines()
print(line2)

f.close()