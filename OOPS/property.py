class Student:
    def __init__(self,hin,eng,math):
        self.hin=hin
        self.eng=eng
        self.math=math
        self.percentage=str((self.eng+self.hin+self.math)/3)+"%"
        
    @property
    def calculate(self):
        return str((self.eng+self.hin+self.math)/3)+"%"
        
per1=Student(98,99,76)
print(per1.calculate)

per1.math=99
print(per1.math)
print(per1.calculate)