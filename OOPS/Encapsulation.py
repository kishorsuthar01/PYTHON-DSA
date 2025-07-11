class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited ")
        print("total of debited amount is ",self.get_balance())
        
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was debited ")
        print("total of credited amount is ",self.get_balance())
        
    def get_balance(self):
        return self.balance
        
    
acc1=Account(20000,12345)
acc1.debit(1000)
acc1.credit(300)

        