#static methods dont use self parameter
class Student:
    @staticmethod #decorator - it allows us to wrap extended behaviour of the function without modifying it
    def college():
        print("IEM")

s1=Student()
s1.college()

#abstraction - hiding the implementation details of a class
#encapsulation - wrapping data and methods into single unit(object)