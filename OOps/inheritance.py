# inheritance is child class deriving propertioes of parent class
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped...")
    
class ToyotaCar (Car): # this class inherites from class car
    def __init__(self,brand):
        self.brand=brand

class Fortuner (ToyotaCar): # fortuner class inherites from toyota class
    def __init__(self, type):
        self.type = type
    
car1 = ToyotaCar("fortuner")
car2 =Fortuner("petrol")

print(car1.start(),car2.color)

#types of inheritance - 1) single inheritance - 1 class inherites another
# 2) multilevel inheritance - parent class -> 1st derived car -> 2nd derived class
# 3) multiple inheritance - 2 or more parent class is present for a derived class

class A:
    varA="welcome to A"

class B:
    varB="welcome to B"

class C(A,B):  # multiple inheritance
    varC="welcome to C"

ob = C()
print(ob.varA,ob.varB,ob.varC)