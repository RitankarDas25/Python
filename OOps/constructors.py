# --init__ function is used to create constructor
# all classes have init function by default which is called when instance is created
class Student:
    college_name="IEM" #class attribute
    def __init__(self): # self indicates it belongs to current object(default constructor)
        print(self) #prints object location
        print("constructor")

    def __init__(self,name):# (parameterized constructor)
        print("constructor 2")
        self.name=name
    
#s1=Student() # gives error as python doesnt support constructor overloading , here the 1st constructor is overwriten by second
s2=Student("RD")
print(s2.college_name,Student.college_name)

class Car:
    def __init__(self,model,engine):
        self.model=model
        self.engine=engine

    def show(self): # function
        print(self.model,self.engine)

c1 = Car("verna","v8")
c1.show()