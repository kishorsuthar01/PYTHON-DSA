class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return (22/7) * self.radius **2
    
    def perimeter(self):
        return 2 * (22/7) *self.radius

cir1=Circle(21)
print(cir1.area())

cir1=Circle(21)
print(cir1.perimeter())




class Employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    
    def showDetails(self):
        print("role =",self.role)
        print("department =",self.dep)
        print("sallary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT",100000)
        

emp1=Engineer("kishor",20)
emp1.showDetails()



class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(self,num2):
        return self.price>num2.price
        
or1=Order("papuji",20)
or2=Order("parleji",10)

print(or1>or2)
    