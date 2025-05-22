# create account class with 2 attributes - balance and account no
#create methods for debit,credit,printing balance
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited")
        print("current balance= Rs",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited")
        print("current balance= Rs",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(100000,202525012003)
acc1.debit(1000)
acc1.credit(500)