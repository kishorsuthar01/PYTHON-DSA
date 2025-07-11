
#  Single level inheritance
class Car:
    @staticmethod
    def start():
        print("can is started..")
    @staticmethod
    def stop():
        print("car is stoped...")
        
class Toyota(Car):
    def __init__(self,name):
        self.name=name
       
car1=Toyota("fortuner")
print(car1.start())


# multi-level inheritance

class Car():
    @staticmethod
    def start():
        print("the car is started..")
        
    @staticmethod
    def stop():
        print("the car is stopped..")
        
class Toyota(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(Toyota):
    def __init__(self, type):
        self.type=type
        
        
car1=Fortuner("BMW")
print(car1.type)
car1.start()


#multiple

class A:
    varA="welcome to variable A"
    
class B:
    varB="welcome to variable B"
    
class C(A,B):
    varC="welcome to variable C"
    
c1=C()
print(c1.varC)
print(c1.varA)
print(c1.varB)

    