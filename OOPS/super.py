class Car:
 
    def __init__(self,type):
        self.type=type
    
    @staticmethod
    def start():
        print("car is started..")
        
    @staticmethod
    def stop():
        print("car is stopedd..")

class Toyota(Car):
    def __init__(self,type,name):
        self.name=name
        super().__init__(type)
        
        
car1=Toyota("petroll","fortuner")
print(car1.name)
