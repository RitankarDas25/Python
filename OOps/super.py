#super() is used to access methods of parent class
class Car:
    
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped...")
    
class ToyotaCar (Car): # this class inherites from class car
    def __init__(self,name,type):
        super().__init__(type) # calls parent class constructor
        self.name=name
        super().start() # calls parent class method
        

car1 = ToyotaCar("fortuner","petrol")
print(car1.type)
