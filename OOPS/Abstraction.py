class Car():
    def Accsilator(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.acc=True
        self.brk=True
        print("the car have a started...")

s1=Car()
s1.start()