#private attributes or methods are meant to be used only within the class and are not accessible outside the class
class Account:
    def __init__(self, acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass # using "__" infront of attribute makes it private same can be done with methods to make them private

    
    
acc1 =Account("1234","kmsojn")
 #print(acc1.__acc_pass) #AttributeError: 'Account' object has no attribute '__acc_pass'
        