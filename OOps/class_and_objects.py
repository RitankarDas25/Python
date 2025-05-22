# class is a blueprint for creating object

class Student:
    name="RD"
s1 = Student() # s1 object or instance
print(s1.name)

class Car:
    model="verna"
    engine="v8"
c1 = Car()
print(c1.engine,c1.model)
c2 = Car()
print(c2.engine,c2.model)

#del keyword is used to delete object properties or object itself
del c2.model
# print(c2.model) AttributeError: 'Car' object has no attribute 'model'
del c2
