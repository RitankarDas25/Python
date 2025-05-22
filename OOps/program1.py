#wap to store name and marks in 3 subjects and print average using oops
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        return (sum/len(self.marks))
    
s1= Student("RD",[98,99,97])
print("name : ",s1.name,"avg marks :",s1.average())