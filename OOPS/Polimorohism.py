class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def number(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):
        Real=self.real+num2.real
        Img=self.img+num2.img
        return complex(Real,Img)
    
    def __sub__(self,num2):
        Real=self.real-num2.real
        Img=self.img-num2.img
        return complex(Real,Img)
        

num1=Complex(2,4)
num1.number()

num2=Complex(3,1)
num2.number()

num3=num1-num2
print(num3)