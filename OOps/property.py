# property decorator makes the function act like a attribute of the class
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.chem + self.math + self.phy)/3) + "%"

stu1 =Student(98,97,99)
print(stu1.percentage)
stu1.phy=86
print(stu1.percentage)