class BankAccount:
    bank_name = "ADBL"
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance +=amount
        return f"you have added {amount} and your total balance is now {self.balance}"
    
    def withdraw(self,amount):
        if amount >self.balance:
            return f"you don't have sufficent balance. you have {self.balance}"
        else:
            self.balance -=amount
            return f"your withdrew {amount}. now your balance is {self.balance}"
    
u1 = BankAccount("sj",500)
print(u1.bank_name)
print(u1.owner)
print(u1.deposit(500))
print(u1.withdraw(6000))

        
