class  Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    
    def average(self):
        sum=0
        for val in self.mark:
            sum+=val
        print("hi",self.name,"your average is ",sum/3)
s1=Student("kishor",[33,32,33])
s1.average()

s1.name="kkroxx"
s1.average()