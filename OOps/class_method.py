# class method is a decorator that bounds the attributes and methods to class
# static method cannot access or modify class state but class methods can
class Person:
    name = "XXXX"

    @classmethod
    def changeName(cls,name):
        cls.name=name

    #def changeName(self,name):
    #    self.name=name

p1=Person()
p1.changeName("Ritankar")
print(p1.name)
print(Person.name)